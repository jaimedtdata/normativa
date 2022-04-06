from django.urls import path
from cursos.views import cursos

urlpatterns = [
    path('', cursos, name='cursos'),
]

