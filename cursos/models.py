from django.db import models
from .choices import PROPIEDAD_CHOICES

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=500, blank=False, verbose_name='Titulo del video')
    norma = models.CharField(max_length=200, blank=False, verbose_name='Norma')
    propiedad = models.CharField(choices=PROPIEDAD_CHOICES, blank=False, max_length=2, default='PU', verbose_name='Propiedad Intelectual')
    embed = models.TextField(verbose_name='Embed')
    descripcion = models.TextField(verbose_name='Descripción')
    caratula = models.FileField(upload_to='cursos_caratulas', verbose_name='Caratula', blank=True, null=True,editable=True)
    fecha_publicacion = models.DateField(verbose_name="Fecha de publicación", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo