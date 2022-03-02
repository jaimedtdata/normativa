from django.db import models
from django.views.generic import View
from django.http import JsonResponse

##pruebas
from normas.models import Areas_Normas, Register_Palabraclave, Register_Normativa
from django.shortcuts import render
from .models import Member
from membership.models import APIMember

class ResultSearchAjax(View):

    def get(self, request):
        data = {
            'saludo' : 'hola'
        }

        return JsonResponse(data)

    def post(self, request):
        res =  None
    
        pal_clave = request.POST.get('pal_clave')
        normas = Register_Normativa.objects.filter(keywords__name__icontains=pal_clave).order_by('tipo_norma__order')
        if len(normas)> 0 and len(pal_clave) >0 :
            data = []
            for position in normas:
                item = {
                    'tipo_norma': position.tipo_norma.subcategory_name,
                    'norma': position.norma,
                    'name_denom': position.name_denom,
                    'base_legal': position.base_legal,
                    'document': position.document,
                    'fecha_publi': position.fecha_publi
                    }
                data.append(item)
            res = data
        else:
            res = 'No existen datos para esa palabra ...'
        return JsonResponse({'data':res})

#vista de prueba para la tabla
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
                'tipo_norma': position.normativa.tipo_norma.subcategory_name,
                'norma': position.normativa.norma,
                'name_denom': position.normativa.name_denom,
                'base_legal': position.normativa.base_legal,
                'document': position.normativa.document,
                'fecha_publi': position.normativa.fecha_publi
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