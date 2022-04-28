import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls import reverse_lazy
from cursos.filters import CursoFilter
from cursos.forms import CursoForm
from normas.models import Palabra_Clave_Normas
from django.core.paginator import Paginator
from cursos.models import Curso
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from normas.serializer import keywords_serializer
from datetime import datetime

# Create your views here.
def cursos(request):
    page = request.GET.get('page', 1)

    queryset = Curso.objects.all()
    filter = CursoFilter(request.GET, queryset=queryset)

    queryset = filter.qs
    paginator = Paginator(queryset, 6)
    queryset = paginator.page(page)

    context = {
        'entity': queryset,
        'filter': filter,
        'paginator': paginator,
    }

    return render(request, 'cursos/cursos.html', context)


class CreateCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/crear_curso.html'

    def form_valid(self, form):
        pcs = self.request.POST.getlist('palabras_clave')
        curso = form.save(commit=False)
        curso.save()

        # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
        for pc in pcs:
            objx, created = Palabra_Clave_Normas.objects.get_or_create(
                name=pc.upper())
            objx.cursos.add(curso)

        messages.success(self.request, 'Video Curso Agregado')
        return HttpResponseRedirect(reverse_lazy('cursos'))

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores')
        return super(CreateCurso, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateCurso, self).get_context_data(**kwargs)
        context.update({
            'palabras_clave': Palabra_Clave_Normas.objects.all()
        })

        return context


def ver_curso(request, id):
    context = {
        'curso': Curso.objects.get(id=id)
    }

    return render(request, 'cursos/ver_curso.html', context)


class UpdateCurso(UpdateView):
    model = Curso
    template_name = 'cursos/editar_curso.html'
    form_class = CursoForm

    def get_success_url(self):
        messages.success(self.request, 'Video Curso Editado')
        return reverse("cursos")

    def get_context_data(self, **kwargs):
        curso = Curso.objects.get(pk=self.get_object().id)
        context = super(UpdateCurso, self).get_context_data(**kwargs)
        context.update({
            'palabras_clave': Palabra_Clave_Normas.objects.all(),
            'palabras_clave_curso': curso.keywords.all(),
            'curso_fecha_publicacion': curso.fecha_publicacion.strftime('%Y-%m-%d') if curso.fecha_publicacion else '',
        })

        return context


def eliminar_curso(request, pk):
    Curso.objects.filter(id = pk).delete()
    messages.success(request, 'Video Curso Eliminado')
    return HttpResponseRedirect(reverse_lazy('cursos'))

# * VISTAS PARA PALABRAS CLAVE DE CURSOS
def registrar_palabras_clave_curso(request, pk):
    if request.method=='POST':
        curso = Curso.objects.get(id = pk)
        pcs = request.POST.getlist('palabras_clave')

        # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
        for pc in pcs:
            objx, created = Palabra_Clave_Normas.objects.get_or_create(name = pc.upper())
            objx.cursos.add(curso)

        palabras = [ keywords_serializer(palabra) for palabra in curso.keywords.all() ]

        return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")

def eliminar_palabra_clave_curso(request, pk):
    curso = Curso.objects.get(id = pk)
    pc = request.GET.get('palabra_clave_id')
    pc = Palabra_Clave_Normas.objects.get(id = pc)
    pc.cursos.remove(curso)
    palabras = [ keywords_serializer(palabra) for palabra in curso.keywords.all() ]

    return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")  
