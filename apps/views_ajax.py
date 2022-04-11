from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from django.db import models
from django.views.generic import View
from django.http import JsonResponse

from django.shortcuts import render
from .models import Member
from membership.models import APIMember
from .serializers import MemberCAPSerializer
from .utils import register_cap_users, register_client_user
from .serializers import ErpSerializer, MemberExternalSerializer

from apps.models import UserToken
from apps.email import send_confirm_account




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
            m_user = Member.objects.get(identity=dni)
            #keep user id in the session 
            if not m_user.user.is_active:
                request.session['user_identity']= dni
            #when user exits in Member Model
            data = {
                'msg' : 'Tu dni ya existe, puedes iniciar sesion',
                'dni':dni,
                'activo': m_user.user.is_active
            }
            return JsonResponse({'data':data})
        else:
            #when user exits in erp but still have not account in this platform
            userERP = APIMember.objects.filter(identity=dni).exists()
            if userERP:
                user=APIMember.objects.get(identity=dni)
                #when user meet the conditions
                if user.has_tutition and user.is_enabled and not user.penalty_fee or user.is_client:
                    data = {
                        'msg' : 'Estas en el ERP, solo confirma algunos datos',
                        'cap' : user.cap_num,
                        'client' : user.is_client,
                        'names': user.name_user,
                    }
                    return JsonResponse({'data': data})
                else:
                #when user doesn't meet the conditions
                    data = {
                        'no_access' : "No puedes acceder debido a que tienes alguna multa  o no te encuentras habilitado, para mayor informacion por favor comunicate con el C.A.P.",
                        'names': user.name_user,
                    }
                    return JsonResponse({'data': data})

            
            #when is a external user (doesn't belong to CAP )
            else:
                data = {
                    'msg' : 'Eres usuario externo, necesitas adquirir un plan para registrarte',
                    
                }
                return JsonResponse({'data': data})

class RegisterCapAPIView(APIView):

    def post(self, request):
        #usercap = request.data['cap']
        serializer = MemberCAPSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            member = register_cap_users(cd)
            token = UserToken(user_profile=member)
            send_confirm_account(self.request, token.get_confirm_link(), member.email)
            data = {
                'email': serializer.data['email'],
            }

            return Response({'data':data, 'success':'registro exitoso'}, status=status.HTTP_201_CREATED)
        
        return Response({'data' : serializer.errors, 'error':'tienes un error'}, status=status.HTTP_400_BAD_REQUEST)


# class RegisterExternalUsersAPIView(APIView):

#     def post(self, request):
#         #usercap = request.data['cap']
#         serializer = MemberExternalSerializer(data=request.data)
#         if serializer.is_valid():
#             cd = serializer.validated_data
#             register_client_user(cd)
#             data = {
#                 'names': serializer.data['names'],
#                 'identity': serializer.data['identity'],
#                 'email': serializer.data['email'],
#                 'mobile': serializer.data['mobile'],
#             }

#             return Response({'data':data, 'success':'registro exitoso'}, status=status.HTTP_201_CREATED)
        
#         return Response({'data' : serializer.errors, 'error':'tienes un error'}, status=status.HTTP_400_BAD_REQUEST)

class APIMemberView(APIView):
    #APi to get members from ERP
    def get(self, request):
        members_cap = APIMember.objects.all()
        serializer = ErpSerializer(members_cap, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class APiViewSetERP(viewsets.ModelViewSet):
    queryset = APIMember.objects
    serializer_class = ErpSerializer