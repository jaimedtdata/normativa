from django.db import models

class date_normativa(models.Model):
    title = models.CharField(max_length=150,blank=False,verbose_name='Titulo')
    subtitle = models.TextField(max_length=150,blank=False,verbose_name='Subtitulo')
    description = models.TextField(verbose_name='Descripcion')

    class Meta:
        verbose_name_plural='Busqueda Normativas'
        db_table ='busqueda_normativa'
    
    def __str__(self):
        return self.title