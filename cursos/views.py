from django.shortcuts import render
from cursos.models import Cursos

# Create your views here.
def cursos(request):
    context = {
        'entity' : Cursos.objects.all()
    }

    return render(request, 'cursos/cursos.html', context)

def ver_curso(request, id):
    context = {
        'curso' : Cursos.objects.get(id = id)
    }

    return render(request, 'cursos/ver-curso.html', context)
