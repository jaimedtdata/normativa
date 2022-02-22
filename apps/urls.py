from django.urls import path, re_path
from .views_ajax import ResultSearchAjax, results_normas_prueba
from .views import LoginNuevo


urlpatterns = [
    path('result_search_ajax/', ResultSearchAjax.as_view(), name='result-search-ajax'),
    path('resultados-normas/', results_normas_prueba, name='resultados_normas'),
    path('login-nuevo/', LoginNuevo.as_view(), name='login-nuevo'),

]