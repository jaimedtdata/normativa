import random
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Coments_foro
from normas.models import Areas_Normas, Register_Normativa

def foro(request):

    context = {
        'foro': True,
        'normas': Register_Normativa.objects.all(),
        'area_normas' : Areas_Normas.objects.all(),
        'last_themes': Coments_foro.objects.order_by('-register_date_time')
    }
    return render(request, 'foro/foro.html', context)


def foro_temas(request):
    context = {
        'foro': True,
        'category_list': [],
        'themes': [],
    }
    return render(request, 'foro/foro_temas.html', context)


def foro_comentarios(request, norma_id):

    norma = Register_Normativa.objects.get(id = norma_id)
    
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        print ('POSTBOTON',comentario)
        b = Coments_foro(tema_id=norma_id,user=request.user, coments=comentario)
        print ('POSTBBB',b)
        b.save()

    comentarios_list = Coments_foro.objects.filter(tema_id = norma_id)

    context = {
        'norma' : norma,
        'comentarios_list' : comentarios_list 
    }


    #comentarios_save(f_id)
    #context = {'data': normas}
    #print ('foro_datos',context)
    return render(request, 'foro/foro_comentarios.html', context)

def borrar_comentario_foro(request, norma_id, comentario_id):
    if request.method == "POST":
        comentario = Coments_foro.objects.filter(id = comentario_id)
        comentario.delete()

    return redirect('foro_comentarios', norma_id = norma_id)

def foro_suscribcion(request, norma_id):
    pass

def get_foro_items():
    rpta_areas = Register_Normativa.objects.all()

    return rpta_areas

def get_coments():
	themes = []
	for x in range(1,15):
		themes.append(
			{
				'theme': '',
				'user': '',
				'comment': '',
				'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
			},
		)
	return themes

def search_theme(request):
    theme = request.GET.get('tema')
    area_id = request.GET.get('area_norma')

    if area_id == '0' :
        themes = Register_Normativa.objects.filter(name_denom__icontains=theme )
    else :
        themes = Register_Normativa.objects.filter(name_denom__icontains=theme ).filter(tipo_uso_id = area_id)
    
    themes = [ theme_serializer(theme) for theme in themes ]

    return HttpResponse(json.dumps(themes, default=str), content_type="application/json")

def theme_serializer(themes):
    return {'id': themes.id, 
            'name_denom' : themes.name_denom,  
            'tipo_uso' : themes.tipo_uso.area_name,
            'norma' : themes.norma,
            'fecha_publi' : themes.fecha_publi
            }