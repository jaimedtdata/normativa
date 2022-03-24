import random
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from foro.emails import async_send_email_suscription, send_email_suscription

from foro.exceptions import MyException
from foro.serializer import foro_serializer
from .models import Comentario_Foro, Foro
from normas.models import Areas_Normas, Register_Normativa
from apps.models import Member, UserToken
from django.core.exceptions import ObjectDoesNotExist

def foro(request):

    context = {
        'foros' : Foro.objects.all(),
        'last_comentarios' : Comentario_Foro.objects.order_by('-created')
    }

    return render(request, 'foro/foro.html', context)


# VISTA Y REGISTO DE COMENTARIOS DE FORO
def foro_comentarios(request, foro_id):

    foro = Foro.objects.get(id = foro_id)
    
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        print ('POSTBOTON',comentario)
        b = Comentario_Foro(foro_id = foro_id, user = request.user, comentario = comentario)
        print ('POSTBBB',b)
        b.save()

        emails = [m.email for m in foro.suscripcion_foro.all()];
        async_send_email_suscription(request, emails)

    comentarios_list = Comentario_Foro.objects.filter(foro_id = foro_id)

    # HERMOSAMENTE SIMPLE
    is_suscribed = Member.objects.filter(suscripcion_foro = foro).filter(user_id = request.user.id).exists()

    context = {
        'foro' : foro,
        'comentarios_list' : comentarios_list, 
        'is_suscribed' : is_suscribed
    }

    return render(request, 'foro/foro_comentarios.html', context)

def borrar_comentario_foro(request, foro_id, comentario_id):
    if request.method == "POST":
        comentario = Comentario_Foro.objects.filter(id = comentario_id)
        comentario.delete()

    return redirect('foro_comentarios', foro_id = foro_id)


# SUSCRIPCION Y DESUSCRIPCION DE FORO POR PARTE DE LOS USUARIOS PARTICIPANTES
def foro_suscripcion(request, foro_id):

    if request.method == "POST":
        state = True if request.POST.get('state') == 'true' else False
        foro = Foro.objects.get(id = foro_id)

        try: 
            member = Member.objects.get(user_id = request.user.id)

            if state:
                member.suscripcion_foro.add(foro)
                message = 'Suscrito'
            else:
                member.suscripcion_foro.remove(foro)
                message = 'Desuscrito'

            return HttpResponse(message, 201)
        
        except Member.DoesNotExist:
            message = 'Tiene que ser miembro para estar suscrito'
            return HttpResponse(message, 405)


# PETICION AJAX EN LA PAGINA PRINCIPAL DE FORO
def buscar_foro(request):
    foro = request.GET.get('foro')

    # area_id = request.GET.get('area_norma')
    # if area_id == '0' :
    #     foros = Register_Normativa.objects.filter(name_denom__icontains=foro).filter(es_foro = True)
    # else :
    #     foros = Register_Normativa.objects.filter(name_denom__icontains=foro).filter(tipo_uso_id = area_id).filter(es_foro = True)
    
    foros = Foro.objects.filter(nombre__icontains=foro)
    foros = [ foro_serializer(foro) for foro in foros ]

    return HttpResponse(json.dumps(foros, default=str), content_type="application/json")