from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 4194304 :
        raise ValidationError("El tamaño máximo que puedes subir es  4MB")
    else:
        return value
