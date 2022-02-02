from django.db import models
from django.contrib import admin
from django.apps import apps
#from .models import (Location_Normas)
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
# Create your models here.

"""

 * TABLAS FORO 

"""



class Categories_foro(models.Model):
    category_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Categoria',
        verbose_name='Nombre de Categoria')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '1. Foro Categorias'
    def __str__(self):
        return self.category_name    

class Subcategories_foro(models.Model):
    categories = models.ForeignKey(Categories_foro,
        on_delete=models.CASCADE,)
    subcategory_name = models.CharField(max_length=200, blank=False,
        help_text='Subcategoria',
        verbose_name='Subcategoria')      

    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '2. Foro SubCategorias'
    def __str__(self):
        return self.subcategory_name    

class Themas_foro(models.Model):
    subcategories =  subcategories = models.ForeignKey(Subcategories_foro,
        on_delete=models.CASCADE,)
    themas_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Tema',
        verbose_name='Nombre de Tema')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '3. Foro Temas'
    def __str__(self):
        return self.themas_name   


class Coments_foro(models.Model):
    # themas =  models.ForeignKey(Themas_foro,
    #     on_delete=models.CASCADE,
    #     help_text='Temas', blank=True,
    #     verbose_name='Temas')
    # Tema Referido a id de Norma
    themas = models.PositiveIntegerField(null=True, blank=True,
        help_text='Tema',
        verbose_name='Tema')
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,)
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
        verbose_name_plural = '4. Foro Comentarios'
    def __str__(self):
        return self.coments  

# class Area_interest(models.Model):
    
#     nombre_area = models.CharField(max_length=200, blank=False,
#         help_text='Nombre de Area',
#         verbose_name='Area')      
#     register_date_time = models.DateTimeField(
#         blank=False, null=False, auto_now_add=True,
#         help_text='Fecha de Registro',
#         verbose_name='Fecha de Registro')
#     class Meta:
#         verbose_name_plural = 'Areas de Interes'