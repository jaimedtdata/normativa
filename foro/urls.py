from django.urls import path
from . import views

urlpatterns = [
    path('', views.foro, name='foro'),
    path('temas/', views.foro_temas, name='foro_temas'),
    path('<int:norma_id>/comentarios/', views.foro_comentarios, name='foro_comentarios'),
]