from datetime import datetime

def normas_serializer(norma):
    return {
        'id' : norma.id,
        'norma' : norma.norma,
        'name_denom' : norma.name_denom,
        'base_legal' : norma.base_legal,
        'tipo_norma_id' : norma.tipo_norma_id,
        'tipo_norma' : norma.tipo_norma.name,
        'tipo_uso_id' : norma.subtipo_uso.tipo_uso_id,
        'tipo_uso' : norma.subtipo_uso.tipo_uso.name,
        'subtipo_uso_id' : norma.subtipo_uso.id,
        'subtipo_uso' : norma.subtipo_uso.name,
        'order' : norma.subtipo_uso.tipo_uso.order,
        'articulo' : norma.articulo,
        'estado' : norma.estado,
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
        'universo_id' : tn.universo_id,
    }

def tipos_uso_serializer(tu): #mama
    return {
        'id' : tu.id,
        'name' : tu.name,
        'order' : tu.order,
    }