from django.db import models
from django.views.generic import View
from django.http import JsonResponse



class ResultSearchAjax(View):

    def get(self, request):
        data = {
            'saludo' : 'hola'
        }

        return JsonResponse(data)

    def post(self, request):
        data = {
            'saludo' : 'Bienvenido'
        }

        return JsonResponse(data)