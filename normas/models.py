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

class Topico_Normas(models.Model):
    name = models.CharField(max_length=150, blank=False, verbose_name="Nombre de topico")
    button = models.CharField(max_length=150, blank=False, verbose_name="Texto de botón para topico")
    icono = models.FileField(blank=True, null=True, editable=True, upload_to='iconos_topico_normativa',verbose_name='Icono del topico')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Topico Principal de Norma'

    def __str__(self):
        return self.name

class Tipo_Uso_Normas(models.Model):
    
    name = models.CharField(max_length=200, blank=False, help_text='Nombre de Categoria', verbose_name='Nombre de la Categoria') 
    topico = models.ForeignKey(Topico_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Topico Norma')
    order = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                     blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Tipo de Uso'

    def __str__(self):
        return self.name

class Subtipo_Normas(models.Model):

    name = models.CharField(max_length=150, blank=False, verbose_name="Nombre de subtipo")
    order = models.CharField(max_length=10, blank=True)
    tipo_uso = models.ForeignKey(Tipo_Uso_Normas, blank=True, verbose_name='Tipo Uso', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name_plural = 'Subtipo de Uso'

    def __str__(self):
        return self.name

class Grupo_Tipo_Normas(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name="Grupo de tipo de norma")
    icono = models.FileField(blank=True, null=True, editable=True, upload_to='iconos_grupo_normativa',verbose_name='Icono del grupo')
    order = models.CharField(max_length=10, blank=True)
    topico = models.ForeignKey(Topico_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Topico Norma')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name_plural = 'Grupo de Tipo de Norma'

    def __str__(self):
        return self.name

class Tipo_Normas(models.Model):
    name = models.CharField(max_length=200, blank=False, help_text='Nombre de Tipo de norma',verbose_name='Tipo norma')
    grupo = models.ForeignKey(Grupo_Tipo_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Grupo Norma')
    order = models.CharField(max_length=10, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name_plural = 'Tipo de Norma'

    def __str__(self):
        return self.name
        

class Estado_Normas(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='Estado de norma')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Estado de Norma'

    def __str__(self):
        return self.name   


PROPIEDAD_CHOICES = [
    ('PU', 'Publico'),
    ('PI', 'Propiedad Intelectual'),
]

class Normativa(models.Model):
    norma = models.CharField(blank=False,null=False,max_length=200,verbose_name='Norma')
    denominacion = models.TextField(blank=False,null=False,verbose_name='Denominacion')
    base_legal = models.CharField(blank=False,null=False,max_length=200,verbose_name='Base Legal')
    fecha_publicacion = models.DateField(blank=True,null=True,verbose_name='Publicacion')
    tipo_norma = models.ForeignKey(Tipo_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Tipo de Norma')
    subtipo_uso = models.ManyToManyField(Subtipo_Normas, verbose_name='Subtipo de uso', related_name='normativas', blank=True)
    document = models.FileField(upload_to='Document_normativa',verbose_name='Documentos',null=True,blank=True,editable=True)
    estado = models.ForeignKey(Estado_Normas, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Estado de la Norma')
    propiedad = models.CharField(choices=PROPIEDAD_CHOICES, blank=False, max_length=150, default='PU')
    descripcion = models.CharField(blank=True,null=True,max_length=700,verbose_name='Descripcion')
    articulo = models.CharField(blank=True,null=True,max_length=200,verbose_name='Articulo')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                     blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                     blank=True, null=True)

    class Meta:
        verbose_name_plural='Normativa'

    def __str__(self):
        return self.norma

    
class Palabra_Clave_Normas(models.Model):
    name = models.CharField(blank=False,null=False,unique=True, max_length=200,verbose_name='Nombre Palabra Clave')
    normativas = models.ManyToManyField(Normativa,verbose_name='Normativa',
                                        related_name='keywords', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",
                                        blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización",
                                        blank=True, null=True)
    class Meta:
        verbose_name_plural='Palabras Clave'

    def __str__(self):
        return self.name


class Preguntas_Frecuentes(models.Model):
    tipo_uso = models.ManyToManyField(Tipo_Uso_Normas,verbose_name='Tipo de uso',
                                        related_name='preguntas', blank=True)
    subtipo_uso = models.ManyToManyField(Subtipo_Normas,verbose_name='Subtipo de uso',
                                        related_name='preguntas', blank=True)        
    topico = models.ManyToManyField(Topico_Normas,verbose_name='Topico de norma',
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