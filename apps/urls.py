from django.urls import path, re_path
from .views_ajax import ResultSearchAjax, results_normas_prueba


urlpatterns = [
    path('result_search_ajax/', ResultSearchAjax.as_view(), name='result-search-ajax'),
    path('resultados-normas/', results_normas_prueba, name='resultados_normas'),
]