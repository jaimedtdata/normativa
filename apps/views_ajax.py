from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import models
from django.views.generic import View
from django.http import JsonResponse

from django.shortcuts import render
from .models import Member
from membership.models import APIMember
from .serializers import MemberCAPSerializer
from .utils import register_cap_users, register_external_user
from .serializers import ErpSerializer, MemberExternalSerializer



def get_dni(request):
    if request.method == "GET":
        data = {
            'saludo' : 'hola'
        }
        return JsonResponse(data)

    if request.method == "POST":
        print(request.POST.get('dni'))
        dni=request.POST.get('dni')
        member=Member.objects.filter(identity=dni).exists()
        if member:
            #when user exits in Memeber Model
            data = {
                'msg' : 'Tu dni ya existe, puedes iniciar sesion',
                'dni':dni,
            }
            return JsonResponse({'data':data})
        else:
            #when user exits in erp but still have not account in this platform
            userERP = APIMember.objects.filter(identity=dni).exists()
            if userERP:
                user=APIMember.objects.get(identity=dni)
                data = {
                    'msg' : 'Estas en el ERP, solo confirma algunos datos',
                    'cap' : user.cap_num,
                    'names': user.name_user,
                }
                return JsonResponse({'data': data})
            
            #when is a external user (doesn't belong to CAP )
            else:
                data = {
                    'msg' : 'Eres usuario externo, necesitas registrarte',
                    
                }
                return JsonResponse({'data': data})

class RegisterCapAPIView(APIView):

    def post(self, request):
        #usercap = request.data['cap']
        serializer = MemberCAPSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            register_cap_users(cd)
            data = {
                'email': serializer.data['email'],
            }

            return Response({'data':data, 'success':'registro exitoso'}, status=status.HTTP_201_CREATED)
        
        return Response({'data' : serializer.errors, 'error':'tienes un error'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterExternalUsersAPIView(APIView):

    def post(self, request):
        #usercap = request.data['cap']
        serializer = MemberExternalSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            register_external_user(cd)
            data = {
                'names': serializer.data['names'],
                'identity': serializer.data['identity'],
                'email': serializer.data['email'],
                'mobile': serializer.data['mobile'],
            }

            return Response({'data':data, 'success':'registro exitoso'}, status=status.HTTP_201_CREATED)
        
        return Response({'data' : serializer.errors, 'error':'tienes un error'}, status=status.HTTP_400_BAD_REQUEST)

class APIMemberView(APIView):
    #APi to get members from ERP
    def get(self, request):
        members_cap = APIMember.objects.all()
        serializer = ErpSerializer(members_cap, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        