from django.urls import path
from .views import foro, foro_temas, foro_comentarios, search_theme, borrar_comentario_foro, foro_suscripcion

urlpatterns = [
    path('', foro, name='foro'),
    path('temas/', foro_temas, name='foro_temas'),
    path('<int:norma_id>/comentarios/', foro_comentarios, name='foro_comentarios'),
    path('search/', search_theme, name="search"),
    path('<int:norma_id>/borrar-comentario/<int:comentario_id>', borrar_comentario_foro, name="borrar-comentario"),
    path('<int:norma_id>/suscripcion', foro_suscripcion, name="foro-suscripcion"),
]