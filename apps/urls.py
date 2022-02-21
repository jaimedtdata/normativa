from django.urls import path, re_path
from .views_ajax import ResultSearchAjax


urlpatterns = [
    path('result_search_ajax/', ResultSearchAjax.as_view(), name='result-search-ajax'),
]