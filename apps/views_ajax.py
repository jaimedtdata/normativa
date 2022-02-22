from django.db import models
from django.views.generic import View
from django.http import JsonResponse

##pruebas
from normas.models import Areas_Normas, Register_Palabraclave, Register_Normativa
from django.shortcuts import render


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

def results_normas_prueba(request):
    if request.method=='POST':
        pal_clave=request.POST['pal_clave'].upper()
        norma_tipo_uso=request.POST['tipo_uso'].upper()
        area_normas=Areas_Normas.objects.all()

        norma_clave=Register_Palabraclave.objects.filter(name__icontains=pal_clave).order_by('normativa__tipo_norma__order')
        count_results= Register_Palabraclave.objects.filter(name=pal_clave).count()
        
        
        normas_results = []
        for n in norma_clave:
            row ={
                'tipo_norma': n.normativa.tipo_norma.subcategory_name,
                'norma': n.normativa.norma,
                'name_denom': n.normativa.name_denom,
                'base_legal': n.normativa.base_legal,
                'document': n.normativa.document,
                'fecha_publi': n.normativa.fecha_publi
            }
            normas_results.append(row)
        
        

        context={ 
            'pal_clave'  : pal_clave,
            'norma_clave':norma_clave,
            #'normativa':normativa,
            'area_normas':area_normas,
            'count_results': count_results,
            'normas_results' : normas_results
        }

        return render(request,'ajax/result.html',context)

    if request.method == 'GET':
        return render(request, 'ajax/result.html')