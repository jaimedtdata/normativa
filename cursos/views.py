from django.shortcuts import render

from cursos.models import Cursos

# Create your views here.
def cursos(request):
    context = {
        'entity' : Cursos.objects.all()
    }

    return render(request, 'cursos/cursos.html', context)