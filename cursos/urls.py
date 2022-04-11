from django.urls import path
from cursos.views import cursos, ver_curso

urlpatterns = [
    path('', cursos, name='cursos'),
    path('<int:id>', ver_curso, name='ver-curso'),

]

