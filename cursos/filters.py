from django import forms
from datetime import datetime
from django.db.models import Q
import django_filters
from normas.models import Palabra_Clave_Normas
from .models import Curso

class CursoFilter(django_filters.FilterSet):

    contenido = django_filters.CharFilter(label="Titulo o descripción", method = 'titulo_or_descripcion_filter')
    palabras_clave = django_filters.MultipleChoiceFilter(label="Palabras clave", method = 'palabras_clave_filter', 
                                                        choices=Palabra_Clave_Normas.objects.values_list('id', 'name'),  
                                                        widget=forms.SelectMultiple(attrs={'class': 'select-multiple', 'style' : 'width:100%;'}))
    rango_fechas = django_filters.CharFilter(label="Rango de fechas", method = 'rango_fechas_filter', 
                                            widget=forms.DateInput( attrs={'data-language':'es','placeholder': '--- RANGO DE FECHAS ---', 'class':'datepicker-here text-center'}))


    class Meta:
        model = Curso
        fields = ['contenido', 'palabras_clave', 'rango_fechas']
    
    def titulo_or_descripcion_filter(self, queryset, name, value):
        return queryset.filter(Q(titulo__icontains = value) | Q(descripcion__icontains = value))

    def palabras_clave_filter(self, queryset, name, value):
        return queryset.filter(keywords__in=value)

    def rango_fechas_filter(self, queryset, name, value):
        value = value.split(" - ")
        date_1 = datetime.strptime(value[0], '%d/%m/%Y')
        date_2 = datetime.strptime(value[1], '%d/%m/%Y')

        return queryset.filter(fecha_publicacion__gte = date_1 ).filter(fecha_publicacion__lte = date_2 )