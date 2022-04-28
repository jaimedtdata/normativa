from dataclasses import fields
from django import forms
from foro.models import Comentario_Foro

class EditComentForo(forms.ModelForm):
    class Meta:
        model = Comentario_Foro
        fields = ['comentario']