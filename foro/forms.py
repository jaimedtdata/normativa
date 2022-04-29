from dataclasses import fields
from django import forms
from foro.models import Comentario_Foro
from django.core.exceptions import ValidationError


FORM_CONTROL = {'class': 'form-control'}
USER_CONTROL = {'class': 'form-control', 'placeholder':'Ingrese CAP o email'}
COMENTARIO_CONTROL = {'class': 'form-control', 'placeholder':'Agrege aqui un comentario'}
class EditComentForo(forms.ModelForm):
    class Meta:
        model = Comentario_Foro
        fields = ['comentario', 'file_one', 'file_two', 'file_three', 'file_four']
        widgets = {
                    'comentario': forms.TextInput(attrs=COMENTARIO_CONTROL, )
                    
                }