import django_filters
from datetime import datetime
from django.db.models import Q
from normas.models import Policies_usage, Register_Normativa

class PoliciesFilter(django_filters.FilterSet):

    content = django_filters.CharFilter(method = 'title_or_message')
    tipo_uso = django_filters.CharFilter(method = 'tipo_uso_order')
    datetimes = django_filters.CharFilter(method = 'date_range')

    class Meta:
        model = Policies_usage
        fields = ['content', 'tipo_uso', 'datetimes']
    
    def title_or_message(self, queryset, name, value):
        return queryset.filter(Q(title__icontains = value) | Q(message__icontains = value))

    def tipo_uso_order(self, queryset, name, value):
        if value != '0':
            return queryset.filter(tipo_uso__order = value)
        else:
            return queryset.all()

    def date_range(self, queryset, name, value):
        value = value.split(" - ")
        date_1 = datetime.strptime(value[0], '%d-%m-%Y')
        date_2 = datetime.strptime(value[1], '%d-%m-%Y')

        return queryset.filter( validity_date_start__gte = date_1 ).filter(validity_date_finish__lte = date_2 )

class NormativaFilter(django_filters.FilterSet):
    content = django_filters.CharFilter(method = 'norma_nombre_bl')

    class Meta:
        model = Register_Normativa
        fields = ['content']

    def norma_nombre_bl(self, queryset, name, value):
        return queryset.filter(Q(name_denom__icontains = value) | Q(norma__icontains = value) | Q(base_legal__icontains = value))