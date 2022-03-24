from django.urls import path
from .views import NormativaUpdateView, SignedURLView, eliminar_normativa, index, registrar_normativa, registrar_palabras_clave, eliminar_palabras_clave_normativa

from . import views

urlpatterns = [
    path('', index, name="index-normativas" ),
    path('registrar', registrar_normativa, name="registrar-normativa" ),
    path('<int:pk>/actualizar', NormativaUpdateView.as_view(), name="actualizar-normativa" ),
    path('<int:normativa>/eliminar', eliminar_normativa, name="eliminar-normativa" ),
    path('<int:normativa>/registrar-palabras-clave', registrar_palabras_clave, name="registrar-palabras-clave"),
    path('<int:normativa>/eliminar-palabra-clave', eliminar_palabras_clave_normativa, name="eliminar-palabras-clave-normativa"),
    path('signed-url/', SignedURLView.as_view(), name='signed-url'),
]