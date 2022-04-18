from django.db import models

# Create your models here.
class Cursos(models.Model):
    titulo = models.CharField(max_length=200, blank=False, verbose_name='Titulo del video')
    embed = models.TextField()
    caratula = models.FileField(upload_to='caratulas',verbose_name='Caratula',null=True,editable=True)
    descripcion = models.CharField(blank=True, null=True, max_length=700, verbose_name='Descripcion del video')
    fecha_publicacioncacion = models.DateTimeField(verbose_name="Fecha de publicación", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo
