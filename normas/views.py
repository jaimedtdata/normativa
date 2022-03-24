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
from normas.filters import NormativaFilter
from django.views.generic.edit import UpdateView
from django.urls import reverse
from normas.forms import NormativaForm
from django.contrib.auth.decorators import login_required

from normas.serializer import keywords_serializer, subtipos_uso_serializer
from .models import Areas_Normas, Register_Normativa, Register_Palabraclave, Subcategories_Normas, Subtipo_Normas

@login_required
def index(request):
    queryset = Register_Normativa.objects.all()
    page = request.GET.get('page', 1)
    filter = NormativaFilter(request.GET, queryset=queryset)

    try:
        queryset = filter.qs
        paginator = Paginator(queryset, 5)
        queryset = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity': queryset,
        'paginator' : paginator,
        'filter' : filter,
    }

    return render(request, 'normativa/index.html', context)

@login_required
def ver_pdf(request, normativa):
    normativa = Register_Normativa.objects.get(id = normativa)
    if normativa.document:
        context = {
            'normativa': normativa
        }

        return render(request, 'normativa/ver_pdf_normativa.html', context)


@login_required
def registrar_normativa(request):
    subtipo_usos = Subtipo_Normas.objects.order_by('order')
    sbu = [ subtipos_uso_serializer(sbu) for sbu in subtipo_usos ]

    context = {
        'form' : NormativaForm,
        'normas': Subcategories_Normas.objects.order_by('order'),
        'tipo_uso': Areas_Normas.objects.order_by('order'),
        'subtipo_uso': subtipo_usos,
        'palabras_clave' : Register_Palabraclave.objects.all(),
        'fecha_hoy' : datetime.today().strftime('%Y-%m-%d'), # para que ? xd
        'subtipos_uso_json' : sbu,
    }

    if request.method=='POST':
        form = NormativaForm(data = request.POST, files = request.FILES)
        
        if form.is_valid():
            normativa = form.save()
            pcs = request.POST.getlist('palabras_clave[]')

            # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
            for pc in pcs:
                objx, created = Register_Palabraclave.objects.get_or_create(name = pc.upper())
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
        norma = Register_Normativa.objects.get(id = normativa)
        pcs = request.POST.getlist('palabras_clave[]')

        # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
        for pc in pcs:
            objx, created = Register_Palabraclave.objects.get_or_create(name = pc)
            objx.normativas.add(norma)

        palabras = get_all_palabras_clave_normativa(norma)

        return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")

class NormativaUpdateView(UpdateView):
    model = Register_Normativa
    # fields = ['norma', 'name_denom', 'base_legal', 'fecha_publi', 'tipo_norma', 'tipo_uso', 'document', 'es_foro', 'es_vigente', 'descripcion']
    template_name = 'normativa/edit_normativa.html'
    form_class = NormativaForm

    def get_success_url(self):
        messages.success(self.request, 'Normativa Editada')
        return reverse("index-normativas")
    
    def get_context_data(self, **kwargs):
        normativa = self.get_object().id
        normativa = Register_Normativa.objects.get(pk = normativa)
        
        context = super(NormativaUpdateView, self).get_context_data(**kwargs)
        subtipos_uso = Subtipo_Normas.objects.order_by('order')
        sbu = [ subtipos_uso_serializer(sbu) for sbu in subtipos_uso ]
        
        context.update({
            'normativa': normativa,
            'subtipo_uso':  subtipos_uso,
            'subtipos_uso_json' : sbu,
            'tipo_normativa': Subcategories_Normas.objects.order_by('order'),
            'tipo_uso': Areas_Normas.objects.order_by('order'),
            'palabras_clave' : Register_Palabraclave.objects.all(),
            'palabras_claves_normativa' : normativa.keywords.all(),
            'fecha_hoy' : datetime.today().strftime('%Y-%m-%d'),
        })
        
        return context

@login_required
def eliminar_normativa(request, normativa):
    Register_Normativa.objects.filter(id = normativa).delete()
    messages.success(request, 'Normativa Eliminada')
    return redirect('/normativas/')


# * VISTAS PARA PALABRAS CLAVE DE NORMATIVAS
@login_required
def eliminar_palabras_clave_normativa(request, normativa):
    norma = Register_Normativa.objects.get(id = normativa)
    pc = request.GET.get('palabra_clave_id')
    pc = Register_Palabraclave.objects.get(id = pc)
    pc.normativas.remove(norma)
    palabras = get_all_palabras_clave_normativa(norma)

    return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")  

@login_required
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