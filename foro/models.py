from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""

 * TABLAS FORO 

"""

class Foro(models.Model):
    nombre = models.CharField(max_length=200, blank=False, verbose_name='Nombre del foro')
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Foro'

    def __str__(self):
        return self.nombre

class Comentario_Foro(models.Model):
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200, blank=False, verbose_name='Comentario')

    likes = models.PositiveSmallIntegerField(default=0,help_text='Likes', verbose_name='Likes')
    dislikes = models.PositiveSmallIntegerField(default=0,help_text='Dislikes', verbose_name='Dislikes')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.comentario  
