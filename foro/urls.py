from django.urls import path
from .views import foro, foro_comentarios, buscar_foro, borrar_comentario_foro, foro_suscripcion, editar_comentario_foro

urlpatterns = [
    path('', foro, name='foro'),
    path('<int:foro_id>/comentarios/', foro_comentarios, name='foro_comentarios'),
    path('search/', buscar_foro, name="search"),
    path('<int:foro_id>/borrar-comentario/<int:comentario_id>', borrar_comentario_foro, name="borrar-comentario"),
    path('<int:foro_id>/suscripcion', foro_suscripcion, name="foro-suscripcion"),
    path('<int:foro_id>/editar-comentario/<int:comentario_id>', editar_comentario_foro, name="editar-comentario"),
]