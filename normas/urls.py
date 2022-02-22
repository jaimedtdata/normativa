from django.urls import path

from . import views

urlpatterns = [
    path('<int:normativa>/palabras-clave', views.palabras_clave, name="palabras-clave"),
    path('<int:normativa>/registrar-palabras-clave', views.registrar_palabras_clave, name="registrar-palabras-clave"),
    path('<int:normativa>/eliminar-palabra-clave', views.eliminar_palabras_clave_normativa, name="eliminar-palabras-clave-normativa")
]