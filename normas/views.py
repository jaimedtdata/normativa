import json
import uuid
from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.contrib import messages
from normas.filters import NormativaFilter

from normas.serializer import keywords_serializer
from .models import Areas_Normas, Register_Normativa, Register_Palabraclave, Subcategories_Normas

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

def form_normativa(request):
    normativa = Subcategories_Normas.objects.order_by('order')
    tipo_uso=Areas_Normas.objects.order_by('area_name')
    palabras_clave = Register_Palabraclave.objects.all()
    context = {
            'normativa':normativa,
            'tipo_uso':tipo_uso,
            'palabras_clave' : palabras_clave,
            'fecha_hoy' : datetime.today().strftime('%Y-%m-%d')
        }
        
    return render(request, 'normativa/form_normativa.html', context)

def registrar_normativa(request):
    if request.method=='POST':
        norma=request.POST['norma']
        name_deno=request.POST['name_deno']
        base_legal=request.POST['base_legal']
        fecha_publi=request.POST['fecha_publi']
        tip_norma=request.POST['tip_norma']
        tip_uso=request.POST['tip_uso']
        file_pdf= request.FILES.get('documento', None)
        es_foro = True if request.POST.get('es_foro', False) == 'on' else False
        es_vigente = True if request.POST.get('es_vigente', False) == 'on' else False
        descripcion = request.POST['descripcion']
        pcs = request.POST.getlist('palabras_clave[]')

        normativa = Register_Normativa.objects.create(norma=norma,name_denom=name_deno,base_legal=base_legal,
                    fecha_publi=fecha_publi,tipo_norma_id=tip_norma,tipo_uso_id=tip_uso,document=file_pdf,es_foro=es_foro, es_vigente=es_vigente, descripcion=descripcion)

        # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
        for pc in pcs:
            objx, created = Register_Palabraclave.objects.get_or_create(name = pc.upper())
            objx.normativas.add(normativa)

        messages.success(request, 'Normativa Creada')
        return redirect("/normativas/")

# Create your views here.
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

def editar_normativa(request, normativa):
    normativa=Register_Normativa.objects.get(pk = normativa)
    tipo_uso=Areas_Normas.objects.order_by('area_name')
    tipo_normativa=Subcategories_Normas.objects.order_by('order')
    palabras_clave = Register_Palabraclave.objects.all()
    palabras_claves_normativa = normativa.keywords.all()

    context = {
        'normativa':normativa,
        'tipo_uso':tipo_uso,
        'tipo_normativa':tipo_normativa,
        'palabras_clave' : palabras_clave,
        'palabras_claves_normativa' : palabras_claves_normativa,
        'fecha_hoy' : datetime.today().strftime('%Y-%m-%d')

    }

    return render(request,'normativa/edit_normativa.html',context)

def actualizar_normativa(request, normativa):
    if request.method=='POST':
        norma=request.POST['norma']
        name_deno=request.POST['name_deno']
        base_legal=request.POST['base_legal']
        fecha_publi=request.POST['fecha_publi']
        tip_norma=request.POST['tip_norma']
        tip_uso=request.POST['tip_uso']
        es_foro = True if request.POST.get('es_foro', False) == 'on' else False
        es_vigente = True if request.POST.get('es_vigente', False) == 'on' else False
        descripcion = request.POST['descripcion']

        
        file_pdf = request.FILES.get('documento', None)

        if file_pdf != None:
            fs = FileSystemStorage()
            file_pdf.name = f'{normativa}-{file_pdf.name}'
            Register_Normativa.objects.get(id=normativa).document.delete()
            filename = fs.save('Document_normativa/' + file_pdf.name, file_pdf)
            file_pdf = filename

        Register_Normativa.objects.filter(id=normativa).update(norma=norma,name_denom=name_deno,base_legal=base_legal,
        fecha_publi=fecha_publi,tipo_norma_id=tip_norma,tipo_uso_id=tip_uso,document=file_pdf,es_foro=es_foro, es_vigente=es_vigente, descripcion=descripcion)


        messages.success(request, 'Normativa Editada')

        return redirect('/normativas/')

def eliminar_normativa(request, normativa):
    Register_Normativa.objects.filter(id = normativa).delete()
    messages.success(request, 'Normativa Eliminada')
    return redirect('/normativas/')


# * VISTAS PARA PALABRAS CLAVE DE NORMATIVAS
def eliminar_palabras_clave_normativa(request, normativa):
    norma = Register_Normativa.objects.get(id = normativa)
    pc = request.GET.get('palabra_clave_id')
    pc = Register_Palabraclave.objects.get(id = pc)
    pc.normativas.remove(norma)
    palabras = get_all_palabras_clave_normativa(norma)

    return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")  

def get_all_palabras_clave_normativa(norma):
        palabras_clave_normativa = norma.keywords.all()
        palabras = [ keywords_serializer(palabra) for palabra in palabras_clave_normativa ]

        return palabras
       
