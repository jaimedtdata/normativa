from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=200, blank=False, verbose_name='Titulo del video')
    embed = models.TextField()
    descripcion = models.CharField(blank=True, null=True, max_length=700, verbose_name='Descripcion del video')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre
