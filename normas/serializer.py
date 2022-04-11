from datetime import datetime

def normas_serializer(norma):
    return {
        'id' : norma.id,
        'norma' : norma.norma,
        'name_denom' : norma.name_denom,
        'base_legal' : norma.base_legal,
        'tipo_norma_id' : norma.tipo_norma_id,
        'tipo_norma' : norma.tipo_norma.name if norma.tipo_norma else None,
        'tipos_uso': [x.tipo_uso.name for x in norma.subtipo_uso.all()],
        'subtipos_uso': [x.name for x in norma.subtipo_uso.all()],
        'tipos_uso_id' : [x.tipo_uso_id for x in norma.subtipo_uso.all()],
        'subtipos_uso_id' : [x.id for x in norma.subtipo_uso.all()],
        'articulo' : norma.articulo if norma.articulo else '',
        'estado' : norma.estado.name,
        'descripcion' : norma.descripcion if norma.descripcion else '',
        'document' : norma.document.url if norma.document else False,
        'fecha_publi' : norma.fecha_publi.strftime('%Y-%m-%d'),
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
    }

def tipo_norma_serializer(tn):
    return {
        'id' : tn.id,
        'name' : tn.name,
        'order' : tn.order,
        'grupo_id' : tn.grupo_id,
        'topico_id' : tn.grupo.universo_id if tn.grupo else 0,
    }

def tipos_uso_serializer(tu): #mama
    return {
        'id' : tu.id,
        'name' : tu.name,
        'order' : tu.order,
    }