from django.db import models
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
    order = models.CharField(max_length=10, blank=True)
    register_date_time = models.DateTimeField(
    blank=False, null=False, auto_now_add=True,
    help_text='Fecha de Registro',
    verbose_name='Fecha de Registro')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                     blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Tipo de Uso'

    def __str__(self):
        return self.area_name

class Subcategories_Normas(models.Model):
    
    subcategory_name = models.CharField(max_length=200, blank=False,
        help_text='Nombre de sub Categoria',
        verbose_name='sub Categoria')      
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    order = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Subtipo De Normativa'
    def __str__(self):
        return self.subcategory_name    

class Register_Normativa(models.Model):
    norma=models.CharField(blank=False,null=False,max_length=200,verbose_name='Norma')
    name_denom = models.TextField(blank=False,null=False,verbose_name='Denominacion')
    base_legal=models.CharField(blank=False,null=False,max_length=200,verbose_name='Base Legal')
    fecha_publi = models.DateField(blank=False,null=False,verbose_name='Publicacion')
    tipo_norma = models.ForeignKey(Subcategories_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Tipo de Norma')
    tipo_uso = models.ForeignKey(Areas_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Tipo Uso')
    document=models.FileField(upload_to='Document_normativa',verbose_name='Documentos',null=True,editable=True)
    es_foro=models.BooleanField(default=False, verbose_name='Es un foro')
    es_vigente=models.BooleanField(default=False, verbose_name='Esta vigente')
    descripcion = models.CharField(blank=True,null=True,max_length=200,verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural='Normativas'
        db_table='register_normativa'

    def __str__(self):
        return self.norma
    
class Register_Palabraclave(models.Model):
    name = models.CharField(blank=False,null=False,unique=True, max_length=200,verbose_name='Nombre Palabra Clave')
    normativas = models.ManyToManyField(Register_Normativa,verbose_name='Normativa',
                                        related_name='keywords', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                        blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                        blank=True, null=True)
    class Meta:
        verbose_name_plural='Palabras Clave'
        db_table='register_palabclave'

    def __str__(self):
        return self.name


class Policies_usage(models.Model):
    tipo_uso = models.ManyToManyField(Areas_Normas,verbose_name='Tipo de uso',
                                        related_name='preguntas', blank=True)
    title = models.CharField(max_length=200, blank=False,
        help_text='Titulo de Consulta',
        verbose_name='Titulo de Consulta')      
    message = models.TextField(blank=False,
        help_text='Respuesta',
        verbose_name='Respuesta')      
    validity_date_start = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Inicio',
        verbose_name='Fecha Inicio')
    validity_date_finish = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha Fin',
        verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')

    class Meta:
        verbose_name_plural = 'Preguntas Frecuentes'

    def __str__(self) -> str:
        return self.title
