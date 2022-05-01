import random
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from foro.emails import async_send_email_suscription, send_email_suscription

from foro.exceptions import MyException
from foro.serializer import foro_serializer
from .models import Comentario_Foro, Foro
from normas.models import Tipo_Uso_Normas, Normativa
from apps.models import Member, UserToken
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import EditComentForo
from django.contrib import messages

@login_required
def foro(request):

    context = {
        'foros' : Foro.objects.all(),
        'last_comentarios' : Comentario_Foro.objects.order_by('-created')
    }

    return render(request, 'foro/foro.html', context)


# VISTA Y REGISTO DE COMENTARIOS DE FORO
@login_required
def foro_comentarios(request, foro_id):
    form = EditComentForo() 
    foro = Foro.objects.get(id = foro_id)
    
    if request.method == "POST":
        # comentario = request.POST.get('comentario')
        # print ('POSTBOTON',comentario)
        # b = Comentario_Foro(foro_id = foro_id, user = request.user, comentario = comentario)
        # print ('POSTBBB',b)
        # b.save()
        form = EditComentForo(data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            cm = Comentario_Foro(foro_id = foro_id, user = request.user,
                                 comentario = cd['comentario'], file_one=cd['file_one'])
            cm.save()
            messages.success(request, "Comentario añadido")

            emails = [m.email for m in foro.suscripcion_foro.all()];
            async_send_email_suscription(request, emails, request.get_full_path())
            
            return redirect('foro_comentarios', foro_id = foro_id)
        else:
            messages.error(request, "El tamaño máximo que puedes subir es  4MB")


    comentarios_list = Comentario_Foro.objects.filter(foro_id = foro_id)

    # HERMOSAMENTE SIMPLE
    is_suscribed = Member.objects.filter(suscripcion_foro = foro).filter(user_id = request.user.id).exists()

    context = {
        'foro' : foro,
        'comentarios_list' : comentarios_list, 
        'is_suscribed' : is_suscribed,
        'form' : form
    }

    return render(request, 'foro/foro_comentarios.html', context)

@login_required
def borrar_comentario_foro(request, foro_id, comentario_id):
    if request.method == "POST":
        comentario = Comentario_Foro.objects.filter(id = comentario_id)
        comentario.delete()

    return redirect('foro_comentarios', foro_id = foro_id)

@login_required
def editar_comentario_foro(request, foro_id, comentario_id):
    foro = get_object_or_404(Foro, id = foro_id)
    comentario = get_object_or_404(Comentario_Foro, id=comentario_id)
    form = EditComentForo(instance=comentario ) 
    data = {
        'foro': foro,
        'comentario': comentario,
        'form' : form
    }

    if request.method == "POST":
        form = EditComentForo(data=request.POST, files=request.FILES, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentario modificado correctamente")
            return redirect('foro_comentarios', foro_id = foro_id)
        else:
            messages.error(request, "El tamaño máximo que puedes subir es  4MB")

    return render(request, 'foro/editar_comentario.html', data)

# SUSCRIPCION Y DESUSCRIPCION DE FORO POR PARTE DE LOS USUARIOS PARTICIPANTES
@login_required
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
@login_required
def buscar_foro(request):
    foro = request.GET.get('foro')

    # area_id = request.GET.get('area_norma')
    # if area_id == '0' :
    #     foros = Normativa.objects.filter(denominacion__icontains=foro).filter(es_foro = True)
    # else :
    #     foros = Normativa.objects.filter(denominacion__icontains=foro).filter(tipo_uso_id = area_id).filter(es_foro = True)
    
    foros = Foro.objects.filter(nombre__icontains=foro)
    foros = [ foro_serializer(foro) for foro in foros ]

    return HttpResponse(json.dumps(foros, default=str), content_type="application/json")