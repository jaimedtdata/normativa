from django import forms
import django_filters
from datetime import datetime
from django.db.models import Q
from normas.models import Preguntas_Frecuentes, Tipo_Normas

class PreguntasFilter(django_filters.FilterSet):

    contenido = django_filters.CharFilter(label="Titulo o Descripción", method = 'titulo_or_descripcion_filter')
    tipos_norma = django_filters.MultipleChoiceFilter(label="Tipo de Norma:", method = 'tipos_norma_filter',
                                                        choices=Tipo_Normas.objects.values_list('id', 'name'),
                                                        widget=forms.SelectMultiple(attrs={'class': 'select-multiple', 'style' : 'width:100%;'}))
    rango_fechas = django_filters.CharFilter(label="Rango de fechas", method = 'rango_fechas_filter',
                                            widget=forms.DateInput( attrs={'data-language':'es','placeholder': '--- RANGO DE FECHAS ---', 'class':'datepicker-here text-center'}))

    class Meta:
        model = Preguntas_Frecuentes
        fields = ['contenido', 'tipos_norma', 'rango_fechas']
    
    def titulo_or_descripcion_filter(self, queryset, name, value):
        return queryset.filter(Q(title__icontains = value) | Q(message__icontains = value))

    def tipos_norma_filter(self, queryset, name, value):
        return queryset.filter(tipo_norma__in=value)

    def rango_fechas_filter(self, queryset, name, value):
        value = value.split(" - ")
        date_1 = datetime.strptime(value[0], '%d/%m/%Y')
        date_2 = datetime.strptime(value[1], '%d/%m/%Y')

        return queryset.filter( validity_date_start__gte = date_1 ).filter(validity_date_finish__lte = date_2 )