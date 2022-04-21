from datetime import datetime
import json


def group_by_duplicate(array):
    sublists = []

    for item in array:
        if item not in sublists:
            sublists.append(item)

    return sublists



def normas_serializer(norma):
    return {
        'id' : norma.id,
        'norma' : norma.norma,
        'denominacion' : norma.denominacion,
        'base_legal' : norma.base_legal,
        'tipo_norma_id' : norma.tipo_norma_id,
        'tipo_norma' : norma.tipo_norma.name,
        'tipos_uso': group_by_duplicate([x.tipo_uso.name for x in norma.subtipo_uso.all()]),
        'subtipos_uso': group_by_duplicate([x.name for x in norma.subtipo_uso.all()]),
        'tipos_uso_id' : [x.tipo_uso_id for x in norma.subtipo_uso.all()],
        'subtipos_uso_id' : [x.id for x in norma.subtipo_uso.all()],
        'articulo' : norma.articulo if norma.articulo else '',
        'estado' :norma.estado.name if norma.estado else '',
        'descripcion' : norma.descripcion if norma.descripcion else '',
        'document' : norma.document.url if norma.document else False,
        'fecha_publicacion' : norma.fecha_publicacion.strftime('%Y-%m-%d') if norma.fecha_publicacion else '',
        'palabras_clave' : [k.id for k in norma.keywords.all()],
    }

def keywords_serializer(palabra):
    return {
        'id' : palabra.id,
        'name' : palabra.name
        }

def subtipos_uso_serializer(sbu):
    return {
        'id' : sbu.id,
        'name' : sbu.name,
        'order' : sbu.order,
        'tipo_uso_id' : sbu.tipo_uso_id,
        'topico_id' : sbu.tipo_uso.topico_id,
    }

def tipo_norma_serializer(tn):
    return {
        'id' : tn.id,
        'name' : tn.name,
        'order' : tn.order,
        'grupo_id' : tn.grupo_id,
        'topico_id' : tn.grupo.topico_id if tn.grupo else 0,
    }

def tipos_uso_serializer(tu): #mama
    return {
        'id' : tu.id,
        'name' : tu.name,
        'order' : tu.order,
        'topico_id' : tu.topico_id,
    }