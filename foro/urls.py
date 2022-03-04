from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro, name='foro'),
    path('temas/', views.foro_temas, name='foro_temas'),
    path('<int:norma_id>/comentarios/', views.foro_comentarios, name='foro_comentarios'),
    path('search/', views.search_theme, name="search"),
    path('<int:norma_id>/borrar-comentario/<int:comentario_id>', views.borrar_comentario_foro, name="borrar-comentario"),
    path('<int:norma_id>/suscribcion', views.foro_suscribcion, name="foro-suscribcion"),
]