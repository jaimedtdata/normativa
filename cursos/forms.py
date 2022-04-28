from django import forms
from django.core.validators import FileExtensionValidator
from cursos.models import Curso
from normas.models import Palabra_Clave_Normas
from cursos.choices import PROPIEDAD_CHOICES

class CursoForm(forms.ModelForm):
    titulo = forms.CharField(label="Título", max_length=500, required=True)
    norma = forms.CharField(label="Norma", max_length=200, required=False)
    caratula = forms.FileField(label="Caratula(350X240)", max_length=200, allow_empty_file=True, required=False)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(), required=False, max_length=700)
    embed = forms.CharField(label="Embed", widget=forms.Textarea(), required=True, max_length=1000)
    propiedad = forms.ChoiceField(label="Propiedad", choices=PROPIEDAD_CHOICES, widget=forms.Select())
    fecha_publicacion = forms.DateField(label="Fecha de Publicación", widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
       model = Curso
       fields = '__all__'