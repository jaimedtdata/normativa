from django import forms
from django.core.validators import FileExtensionValidator
from normas.models import PROPIEDAD_CHOICES, Estado_Normas, Normativa, Subtipo_Normas, Tipo_Normas

class NormativaForm(forms.ModelForm):
    norma = forms.CharField(max_length=200, required=False)
    denominacion = forms.CharField(label="Título", max_length=100)
    base_legal = forms.CharField(label="Base Legal", max_length=200, required=False)
    fecha_publicacion = forms.DateField(label="Fecha de Publicación", widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    tipo_norma = forms.ModelChoiceField(label="Tipo de Norma", queryset=Tipo_Normas.objects.order_by('name'))
    subtipo_uso = forms.ModelMultipleChoiceField(label="Subtipo de Uso", queryset=Subtipo_Normas.objects.all(),  widget=forms.SelectMultiple(attrs={'class': 'select-multiple', 'style' : 'width:100%;'}))
    document = forms.FileField(label="Documento", max_length=100, allow_empty_file=True, required=False)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(), required=False, max_length=700)
    estado = forms.ModelChoiceField(label="Estado", queryset=Estado_Normas.objects.all(), required=False)
    articulo = forms.CharField(label="Articulado", max_length=200, required=False)
    propiedad = forms.ChoiceField(label="Propiedad", choices=PROPIEDAD_CHOICES, widget=forms.Select())

    class Meta:
       model = Normativa
       fields = '__all__'