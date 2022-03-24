def foro_serializer(foro):
    return {
        'id': foro.id, 
        'nombre' : foro.nombre,
        'descripcion' : foro.descripcion,
        'created' : foro.created,
        }