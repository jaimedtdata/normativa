from django.db import models
from django.views.generic import View
from django.http import JsonResponse

##pruebas
from django.shortcuts import render
from .models import Member
from membership.models import APIMember


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
            data = {
                'msg' : 'Tu dni ya existe, puedes iniciar sesion',
                'dni':dni,
            }
            return JsonResponse({'data':data})
        else:
            userERP = APIMember.objects.filter(identity=dni).exists()
            if userERP:
                user=APIMember.objects.get(identity=dni)
                data = {
                    'msg' : 'Estas en el ERP, solo confirma algunos datos',
                    'cap' : user.cap_num,
                    'names': '',
                }
                return JsonResponse({'data': data})
            else:
                data = {
                    'msg' : 'Eres usuario externo, necesitas registrarte',
                    
                }
                return JsonResponse({'data': data})