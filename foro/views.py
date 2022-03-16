import random
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from foro.emails import async_send_email_suscription, send_email_suscription

from foro.exceptions import MyException
from .models import Coments_foro
from normas.models import Areas_Normas, Register_Normativa
from apps.models import Member, UserToken
from django.core.exceptions import ObjectDoesNotExist

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

        emails = [m.email for m in norma.suscripcion_foro.all()];
        async_send_email_suscription(request, emails)

    comentarios_list = Coments_foro.objects.filter(tema_id = norma_id)

    # HERMOSAMENTE SIMPLE
    is_suscribed = Member.objects.filter(suscripcion_foro = norma).filter(user_id = request.user.id).exists()

    context = {
        'norma' : norma,
        'comentarios_list' : comentarios_list, 
        'is_suscribed' : is_suscribed
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

def foro_suscripcion(request, norma_id):

    if request.method == "POST":
        state = True if request.POST.get('state') == 'true' else False
        norma = Register_Normativa.objects.get(id = norma_id)

        try: 
            member = Member.objects.get(user_id = request.user.id)

            if state:
                member.suscripcion_foro.add(norma)
                message = 'Suscrito'
            else:
                member.suscripcion_foro.remove(norma)
                message = 'desuscrito'

            return HttpResponse(message, 201)
        
        except Member.DoesNotExist:
            message = 'Tiene que ser miembro para estar suscrito'
            return HttpResponse(message, 405)

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
        themes = Register_Normativa.objects.filter(name_denom__icontains=theme).filter(es_foro = True)
    else :
        themes = Register_Normativa.objects.filter(name_denom__icontains=theme).filter(tipo_uso_id = area_id).filter(es_foro = True)
    
    themes = [ theme_serializer(theme) for theme in themes ]

    return HttpResponse(json.dumps(themes, default=str), content_type="application/json")

def theme_serializer(themes):
    return {'id': themes.id, 
            'name_denom' : themes.name_denom,  
            'tipo_uso' : themes.tipo_uso.area_name,
            'norma' : themes.norma,
            'fecha_publi' : themes.fecha_publi,
            'es_foro' : themes.es_foro
            }