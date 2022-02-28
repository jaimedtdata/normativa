
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
MEMBERSHIP_CHOICES = [
    ('PNA', 'Plan no Agremiado'),
    ('PLPA', 'Pago en Linea - Plan Agremiado'),
    ('PLPPA', 'Pago en Linea - Plan Premium Agremiado'),
    ('PLPP', 'Pago en Linea - Plan Profesional'),
    ('PPPA', 'Pagos Presenciales - Plan Agremiado'),
    ('PPPPA', 'Pagos Presenciales - Plan Premium Agremiado'),
    ('PPPP', 'Pagos Presenciales - Plan Profesional')
]

class MembershipBenefits(models.Model):
    name = models.CharField(max_length=250, verbose_name='Beneficios de las membresia')
    
    def __str__(self):
       return self.name

    class Meta:
        verbose_name_plural = 'Beneficios de las Membresías'

class Membership(models.Model):
    membership_type = models.CharField(
                choices=MEMBERSHIP_CHOICES, default='PLPA', max_length=30)
    price_month = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    price_year = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    benefits = models.ManyToManyField(MembershipBenefits)
    #Plan por fechas (mdiario, mensual, tri, sem, anual) Foreign
    #fecha de inicio
    #fecha fin
    #precio que se pago mensual
    #precio que se pago anual

    def __str__(self):
       return self.membership_type

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
    name_user = models.CharField(max_length=250, verbose_name='Nombre del usuario')
    cap_num = models.PositiveBigIntegerField(verbose_name='No. de Colegiatura')
    is_enabled = models.BooleanField(default=False, verbose_name='¿Esta habilitado?')
    penalty_fee = models.BooleanField(default=False, verbose_name='¿Tiene multas?')
    has_tutition = models.BooleanField(default=False, verbose_name='¿Es colegiado?')
    identity = models.CharField(max_length=11, blank=True,
        help_text='DNI o RUC',
        verbose_name='Documento de Identidad')
    date_enrollment = models.DateField(verbose_name='fecha de inscripcion', blank=True, null=True)
    date_expired = models.DateField(verbose_name='fecha de caducidad', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.name_user