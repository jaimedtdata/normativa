import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Register_Normativa, Register_Palabraclave

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

def keywords_serializer(palabra):
    return {
        'id' : palabra.id,
        'name' : palabra.name
        }

def get_all_palabras_clave_normativa(norma):
        palabras_clave_normativa = norma.keywords.all()
        palabras = [ keywords_serializer(palabra) for palabra in palabras_clave_normativa ]

        return palabras
       

def eliminar_palabras_clave_normativa(request, normativa):
    norma = Register_Normativa.objects.get(id = normativa)
    pc = request.GET.get('palabra_clave_id')

    pc = Register_Palabraclave.objects.get(id = pc)

    pc.normativas.remove(norma)

    palabras = get_all_palabras_clave_normativa(norma)

    return HttpResponse(json.dumps(palabras, default=str), content_type="application/json")  
    
def palabras_clave(request, normativa):
    pass