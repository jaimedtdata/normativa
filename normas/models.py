from django.db import models
#from sqlalchemy import true
from apps.choices import *
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
# Create your models here.




def upload_file(instance, filename):
    ext = filename.split('.')[-1]
    return 'pdf/{}'.format(instance.file)

def upload_signature(instance, filename):
    ext = filename.split('.')[-1]
    return 'signatures/{}.{}'.format(instance.file, ext)

def upload_photos(instance, filename):
    ext = filename.split('.')[-1]
    return 'photos/{}.{}'.format(instance.identity, ext)




class Areas_Normas(models.Model):
    
    area_name = models.CharField(max_length=200, blank=False, help_text='Nombre de Categoria', verbose_name='Nombre de la Categoria')      
    register_date_time = models.DateTimeField(
    blank=False, null=False, auto_now_add=True,
    help_text='Fecha de Registro',
    verbose_name='Fecha de Registro')
    
    class Meta:
        verbose_name_plural = '0.Normas - Tipo de Uso'

    def __str__(self):
        return self.area_name


class Categories_Normas(models.Model):
    
    category_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Categoria',
        verbose_name='Nombre de la Categoria')      

    area_name = models.ManyToManyField(Areas_Normas,
        help_text='Area Corresponde',
        verbose_name='Area') 

    
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    

    class Meta:
        verbose_name_plural = '1.Normas - Sub Tipo de Uso'
    def __str__(self):
        return self.category_name



class Subcategories_Normas(models.Model):
    
    subcategory_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de sub Categoria',
        verbose_name='sub Categoria')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '2.Normas - Subtipo De Normativa'
    def __str__(self):
        return self.subcategory_name    

class Location_Normas(models.Model):
    
    Location_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre Locacion',
        verbose_name='Locacion')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '3.Normas - Locacion'
    def __str__(self):
        return self.Location_name    

class Master_Normas(models.Model):
    
    area_name = models.ForeignKey(Areas_Normas, on_delete=models.CASCADE,
        help_text='registro de Tipo de Uso',
        verbose_name='Tipo de Uso') 
    category_name = models.ForeignKey(Categories_Normas, on_delete=models.CASCADE,
        help_text='registro Sub Tipo de Uso',
        verbose_name='Sub Tipo de Uso')     
    subcategory_name = models.ForeignKey(Subcategories_Normas, on_delete=models.CASCADE,
        help_text='registro Tipo de Normativa',
        verbose_name='Tipo de Normativa')     
    location_name =  models.ForeignKey(Location_Normas, on_delete=models.CASCADE,
        help_text='Registro de Locacion',
        verbose_name='Locacion')
    norma_rne = models.CharField(max_length=50, blank=True,
        help_text='Nombre RNE - Norma',
        verbose_name='RNE-Norma')
    norma_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Norma',
        verbose_name='Norma')
    validity_date_start = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Publicacion',
        verbose_name='Fecha Publicacion')
    keywords = models.CharField(max_length=200, blank=True,
        help_text='Palabras Clave',
        verbose_name='Registre palabras clave') 
    file = models.FileField(
        upload_to=upload_file, blank=False,
        help_text='Suba el archivo o base legal',
        verbose_name='File')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    class Meta:
        verbose_name_plural = '4.Registrar Normas'
    def __str__(self):
        return self.norma_name 
    
class SubNormativa(models.Model):
    norma=models.CharField(max_length=200,blank=False,verbose_name='Normativa')
    norma_sub=models.ForeignKey(Subcategories_Normas,blank=True,on_delete=models.CASCADE,verbose_name='Sub Normativa')

    class Meta:
        verbose_name_plural='5.Normas-Normativa'

    def __str__(self):
        return self.norma

#johao
class Register_Normativa(models.Model):
    norma=models.CharField(blank=False,null=False,max_length=200,verbose_name='Norma')
    name_denom = models.TextField(blank=False,null=False,verbose_name='Denominacion')
    base_legal=models.CharField(blank=False,null=False,max_length=200,verbose_name='Base Legal')
    fecha_publi = models.DateField(blank=False,null=False,verbose_name='Publicacion')
    tipo_norma=models.CharField(blank=False,null=False,max_length=200,
    verbose_name='Tipo de Norma')
    tipo_uso = models.ForeignKey(Areas_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Tipo Uso', related_name='normas')
    document=models.FileField(upload_to='Document_normativa',verbose_name='Documentos')
    es_foro=models.BooleanField(default=False, verbose_name='Es un foro')

    class Meta:
        verbose_name_plural='6.Normas Registradas-Frontend'
        db_table='register_normativa'
    
class Register_Palabraclave(models.Model):
    name = models.TextField(blank=False,null=False,verbose_name='Nombre Palabra Clave')
    normativa = models.ForeignKey(Register_Normativa,verbose_name='Normativa',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='7.Normas Registradas-Palabras Clave'
        db_table='register_palabclave'
    

#end
