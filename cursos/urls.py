from django.urls import path
from django.contrib.auth.decorators import login_required
from cursos.views import CreateCurso, UpdateCurso, cursos, eliminar_curso, eliminar_palabra_clave_curso, registrar_palabras_clave_curso, ver_curso

urlpatterns = [
    path('', login_required(cursos), name='cursos'),
    path('<int:id>', login_required(ver_curso), name='ver-curso'),
    path('crear/', login_required(CreateCurso.as_view()), name='crear-curso'),
    path('<int:pk>/editar', login_required(UpdateCurso.as_view()), name='editar-curso'),
    path('<int:pk>/eliminar', login_required(eliminar_curso), name='eliminar-curso'),
    path('<int:pk>/eliminar-palabra-clave', login_required(eliminar_palabra_clave_curso), name='eliminar-palabra-clave-curso'),
    path('<int:pk>/registrar-palabras-clave', login_required(registrar_palabras_clave_curso), name="registrar-palabras-clave-curso"),

]

