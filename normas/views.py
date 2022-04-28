import json
import uuid
import boto3

from datetime import datetime

from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from django.views import generic
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse
from normas.forms import NormativaForm
from django.contrib.auth.decorators import login_required

from normas.serializer import keywords_serializer, normas_serializer, subtipos_uso_serializer, tipo_norma_serializer, tipos_uso_serializer
from .models import Estado_Normas, Tipo_Uso_Normas, Grupo_Tipo_Normas, Normativa, Palabra_Clave_Normas, Tipo_Normas, Subtipo_Normas, Topico_Normas

@login_required
def index(request):
    normativas = Normativa.objects.order_by('tipo_norma').order_by('subtipo_uso').order_by('norma')
    tipos_norma = Tipo_Normas.objects.order_by('order')
    tipos_uso = Tipo_Uso_Normas.objects.order_by('name')
    palabras_clave = Palabra_Clave_Normas.objects.all()
    subtipos_uso = Subtipo_Normas.objects.order_by('order')
    topicos = Topico_Normas.objects.all()
    estado = Estado_Normas.objects.all()

    normas = [ normas_serializer(norma) for norma in normativas ]
    tn = [ tipo_norma_serializer(tn) for tn in tipos_norma ]
    sbu = [ subtipos_uso_serializer(sbu) for sbu in subtipos_uso ]
    tu = [ tipos_uso_serializer(tu) for tu in tipos_uso ]

    context={
            'normativas': normativas,
            'tipos_norma': tipos_norma, 
            'tipos_uso' : tipos_uso, 
            'subtipos_uso' : subtipos_uso,
            'palabras_clave' : palabras_clave,
            'estado': estado,
            'normativas_json' : json.dumps(normas),
            'sbu_json' : json.dumps(sbu),
            'tu_json' : json.dumps(tu),
            'tn_json' : tn,
            'topicos' : topicos,
            }

    return render(request, 'normativa/index.html', context)

@login_required
def ver_pdf(request, normativa):
    normativa = Normativa.objects.get(id = normativa)
    if normativa.document:
        context = {
            'normativa': normativa
        }

        return render(request, 'normativa/ver_pdf_normativa.html', context)


@login_required
def registrar_normativa(request):
    tipos_uso = Tipo_Uso_Normas.objects.all()
    tu = [ tipos_uso_serializer(tu) for tu in tipos_uso ]

    subtipo_usos = Subtipo_Normas.objects.order_by('order')
    sbu = [ subtipos_uso_serializer(sbu) for sbu in subtipo_usos ]

    tipo_normas = Tipo_Normas.objects.order_by('order')
    tn = [ tipo_norma_serializer(tn) for tn in tipo_normas ]

    context = {
        'form' : NormativaForm,
        'tipo_uso': Tipo_Uso_Normas.objects.order_by('order'),
        'topico_norma': Topico_Normas.objects.all(),
        'palabras_clave' : Palabra_Clave_Normas.objects.all(),
        'fecha_hoy' : datetime.today().strftime('%Y-%m-%d'), # para que ? xd
        'tipo_norma': tipo_normas, 
        'subtipo_uso': subtipo_usos,
        'subtipos_uso_json' : sbu,
        'tipo_normas_json': tn,
        'tipos_uso_json' : tu,
    }

    if request.method=='POST':
        form = NormativaForm(data = request.POST, files = request.FILES)
        
        if form.is_valid():
            normativa = form.save()
            pcs = request.POST.getlist('palabras_clave[]')

            # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
            for pc in pcs:
                objx, created = Palabra_Clave_Normas.objects.get_or_create(name = pc.upper())
                objx.normativas.add(normativa)

            messages.success(request, 'Normativa Creada')
            return redirect("/normativas/")
            
        else :
            context['form'] = form
        
    return render(request, 'normativa/form_normativa.html', context)

# Create your views here.
@login_required
def registrar_palabras_clave(request, normativa):
    if request.method=='POST':
        norma = Normativa.objects.get(id = normativa)
        pcs = request.POST.getlist('palabras_clave[]')

        # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
        for pc in pcs:
            objx, created = Palabra_Clave_Normas.objects.get_or_create(name = pc.upper())
            objx.normativas.add(norma)

        palabras = get_all_palabras_clave_normativa(norma)

        return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")

class NormativaUpdateView(UpdateView):
    model = Normativa
    template_name = 'normativa/edit_normativa.html'
    form_class = NormativaForm

    def get_success_url(self):
        messages.success(self.request, 'Normativa Editada')
        return reverse("index-normativas")
    
    def get_context_data(self, **kwargs):
        normativa = self.get_object().id
        normativa = Normativa.objects.get(pk = normativa)
        
        context = super(NormativaUpdateView, self).get_context_data(**kwargs)
        tipos_uso = Tipo_Uso_Normas.objects.all()
        tu = [ tipos_uso_serializer(tu) for tu in tipos_uso ]
        
        subtipos_uso = Subtipo_Normas.objects.order_by('order')
        sbu = [ subtipos_uso_serializer(sbu) for sbu in subtipos_uso ]

        tipo_normas = Tipo_Normas.objects.order_by('order')
        tn = [ tipo_norma_serializer(tn) for tn in tipo_normas ]

        tnn = [x.tipo_uso_id for x in normativa.subtipo_uso.all()]
        
        context.update({
            'normativa': normativa,
            'subtipo_uso':  subtipos_uso,
            'subtipos_uso_json' : sbu,
            'tipo_norma': tipo_normas, 
            'topico_norma': Topico_Normas.objects.all(),
            'tipo_uso': Tipo_Uso_Normas.objects.order_by('order'),
            'palabras_clave' : Palabra_Clave_Normas.objects.all(),
            'palabras_claves_normativa' : normativa.keywords.all(),
            'fecha_hoy' : datetime.today().strftime('%Y-%m-%d'),
            'tipo_normas_json': tn,
            'tnn' : json.dumps(tnn),
            'tipos_uso_json' : tu,
        })
        
        return context

@login_required
def eliminar_normativa(request, normativa):
    Normativa.objects.filter(id = normativa).delete()
    messages.success(request, 'Normativa Eliminada')
    return redirect('/normativas/')


# * VISTAS PARA PALABRAS CLAVE DE NORMATIVAS
@login_required
def eliminar_palabras_clave_normativa(request, normativa):
    norma = Normativa.objects.get(id = normativa)
    pc = request.GET.get('palabra_clave_id')
    pc = Palabra_Clave_Normas.objects.get(id = pc)
    pc.normativas.remove(norma)
    palabras = get_all_palabras_clave_normativa(norma)

    return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")  

def get_all_palabras_clave_normativa(norma):
        palabras_clave_normativa = norma.keywords.all()
        palabras = [ keywords_serializer(palabra) for palabra in palabras_clave_normativa ]

        return palabras

class SignedURLView(generic.View):
    def post(self, request, *args, **kwargs):
        session = boto3.session.Session()
        client = session.client(
            "s3",
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        url = client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                "Key": f"normativa_files/{json.loads(request.body)['fileName']}",
            },
            ExpiresIn=300,
        )
        return JsonResponse({"url": url})
