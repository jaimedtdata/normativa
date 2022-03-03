from datetime import datetime

def normas_serializer(norma):
    return {
        'id' : norma.id,
        'norma' : norma.norma,
        'name_denom' : norma.name_denom,
        'base_legal' : norma.base_legal,
        'tipo_norma_id' : norma.tipo_norma_id,
        'tipo_uso_id' : norma.tipo_uso_id,
        'tipo_uso' : norma.tipo_uso.area_name,
        'es_vigente' : norma.es_vigente,
        'descripcion' : norma.descripcion,
        'document' : norma.document.url if norma.document else False,
        'fecha_publi' : norma.fecha_publi.strftime('%Y-%m-%d')
    }

