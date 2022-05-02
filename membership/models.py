
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .choices import MEMBERSHIP_CHOICES, PROFESSION_CHOICES, PERSON_TYPE_CHOICES, PAYMENT_CHOICES
# Create your models here.


class MembershipBenefits(models.Model):
    name = models.CharField(max_length=250, verbose_name='Beneficios de las membresias')
    
    def __str__(self):
       return self.name

    class Meta:
        verbose_name_plural = 'Beneficios de las Membresías'

class MembershipConditions(models.Model):
    name = models.CharField(max_length=250, verbose_name='Condiciones de las membresias')
    
    def __str__(self):
       return self.name

    class Meta:
        verbose_name_plural = 'Condiciones de las Membresías'

class Membership(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, 
                                verbose_name="Nombre del Plan")
    membership_type = models.CharField(
                choices=MEMBERSHIP_CHOICES, default='PLPA', max_length=30)
    price_month = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    price_quarterly = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name="Trimestral")
    price_year = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    benefits = models.ManyToManyField(MembershipBenefits)
    conditions= models.ManyToManyField(MembershipConditions, blank=True)
    #Plan por fechas (mdiario, mensual, tri, sem, anual) Foreign
    #fecha de inicio
    #fecha fin
    #precio que se pago mensual
    #precio que se pago anual

    def __str__(self):
       return f'{self.name} - {self.membership_type}'

    def get_benefits(self):
        return "---\n".join([b.name for b in self.benefits.all()])
    
    class Meta:
        verbose_name_plural = 'Clases de Membresías'


# class Subscription(models.Model):
#     user_membership = models.ForeignKey(Member, related_name='subscription', on_delete=models.CASCADE)
#     active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
#     updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
#     def __str__(self):
#         return self.user_membership.user.username
    

class APIMember(models.Model):
    name_user = models.CharField(max_length=250, 
        verbose_name='Nombre del usuario')
    first_surname= models.CharField(max_length=250, 
        verbose_name='Apellido Paterno', blank=True, null=True)
    second_surname = models.CharField(max_length=250, 
        verbose_name='Apellido Materno', blank=True, null=True)
    cap_num = models.PositiveBigIntegerField(verbose_name='No. de Colegiatura')
    identity = models.CharField(max_length=16, blank=True,
        help_text='DNI o RUC',
        verbose_name='Documento de Identidad')
    person_type = models.CharField(max_length=1, default='N',
        help_text='Tipo de Persona', choices=PERSON_TYPE_CHOICES,
        verbose_name='Tipo de Persona', blank=False)
    profession = models.CharField(max_length=1,
        help_text='Profesión', choices=PROFESSION_CHOICES,
        verbose_name='Profesión', blank=True)
    mobile = models.CharField(max_length=12, blank=True,
        help_text='Número de Teléfono Celular',
        verbose_name='Celular')
    phone = models.CharField(max_length=10, blank=True,
        help_text='Número de Teléfono Fijo o de Oficina',
        verbose_name='Teléfono')
    email = models.EmailField(max_length=50, blank=False, null=False,
        help_text='Correo Electrónico',
        verbose_name='Email')
    secret_code = models.PositiveIntegerField(null=True, blank=True,
        help_text='Código Secreto de Arquitecto',
        verbose_name='Código Secreto de Arquitecto')
    address = models.CharField(max_length=200, blank=True,
        help_text='Dirección',
        verbose_name='Dirección')
    price_month = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)
    price_year = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(choices=PAYMENT_CHOICES, default='V',max_length=10 ,null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='PLPA', max_length=30, blank=True, null=True)

    is_enabled = models.BooleanField(default=False, verbose_name='¿Esta habilitado?')
    penalty_fee = models.BooleanField(default=False, verbose_name='¿Tiene multas?')
    has_tutition = models.BooleanField(default=False, verbose_name='¿Es colegiado?')
    is_client = models.BooleanField(default=False, verbose_name='¿Es cliente?')
    
    date_enrollment = models.DateTimeField(verbose_name='fecha de inscripcion', blank=True, null=True)
    date_expired = models.DateTimeField(verbose_name='fecha de caducidad', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name_user