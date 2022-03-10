import django_filters
from normas.models import Policies_usage

class PoliciesFilter(django_filters.FilterSet):
    class Meta:
        model = Policies_usage
        fields = {'title' : ['icontains'], 'message': ['icontains'], 'tipo_uso': ['exact']}