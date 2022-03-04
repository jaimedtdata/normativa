from django.db import models
from django.contrib import admin
from django.apps import apps
#from .models import (Location_Normas)
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from normas.models import Register_Normativa
# Create your models here.

"""

 * TABLAS FORO 

"""

class Coments_foro(models.Model):
    
    tema = models.ForeignKey(Register_Normativa, on_delete=models.CASCADE, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    coments = models.CharField(max_length=200, blank=False,
        help_text='comentario',
        verbose_name='comentario')

    likes = models.PositiveSmallIntegerField(default=0,help_text='Likes', verbose_name='Likes')
    dislikes = models.PositiveSmallIntegerField(default=0,help_text='Dislikes', verbose_name='Dislikes')
    
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = 'Comentarios'
    def __str__(self):
        return self.coments  
