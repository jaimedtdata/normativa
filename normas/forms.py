from django import forms
from normas.models import UNIVERSO_CHOICES, Register_Normativa, Subcategories_Normas, Subtipo_Normas, ESTADO_CHOICES

class NormativaForm(forms.ModelForm):
    norma = forms.CharField(max_length=200,)
    name_denom = forms.CharField(label="Título", max_length=100)
    base_legal = forms.CharField(label="Base Legal", max_length=200)
    fecha_publi = forms.DateField(label="Fecha de Publicación", widget=forms.DateInput(attrs={'type': 'date'}))
    tipo_norma = forms.ModelChoiceField(label="Tipo de Norma", queryset=Subcategories_Normas.objects.order_by('order'))
    subtipo_uso = forms.ModelChoiceField(label="Subtipo de Uso", queryset=Subtipo_Normas.objects.order_by('order'))
    document = forms.FileField(label="Documento", max_length=100,allow_empty_file=True,required=False)
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(), required=False, max_length=700)
    universo = forms.ChoiceField(choices=UNIVERSO_CHOICES, label="Universo", widget=forms.Select())
    estado = forms.ChoiceField(label="Estado", choices=ESTADO_CHOICES)
    articulo = forms.CharField(label="Articulado", max_length=200, required=False)
    #es_foro = forms.CheckboxInput()

    class Meta:
       model = Register_Normativa
       fields = '__all__'