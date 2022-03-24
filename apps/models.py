import uuid
from django.db import models

from foro.models import Foro
from .choices import *
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from membership.models import Membership


def upload_file(instance, filename):
    ext = filename.split('.')[-1]
    return 'pdf/{}'.format(instance.file)

def upload_signature(instance, filename):
    ext = filename.split('.')[-1]
    return 'signatures/{}.{}'.format(instance.file, ext)

def upload_photos(instance, filename):
    ext = filename.split('.')[-1]
    return 'photos/{}.{}'.format(instance.identity, ext)



"""

 * TABLAS GENERALES 

"""

class Member(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        help_text='Usuario', null=True, blank=True,
        verbose_name='Usuario', related_name='user_membership')
    first_surname = models.CharField(max_length=50, blank=True,
        help_text='Apellido Paterno',
        verbose_name='Apellido Paterno')
    second_surname = models.CharField(max_length=50, blank=True,
        help_text='Apellido Materno',
        verbose_name='Apellido Materno')
    names = models.CharField(max_length=50, blank=False,
        help_text='Nombres O Razón Social',
        verbose_name='Nombres')
    full_name = models.CharField(max_length=200, blank=False,default='Nombre completo',
        help_text='Apellidos y Nombres',
        verbose_name='Apellidos y Nombres')
    person_type = models.CharField(max_length=1, default='N',
        help_text='Tipo de Persona', choices=PERSON_TYPE_CHOICES,
        verbose_name='Tipo de Persona', blank=True)
    identity = models.CharField(max_length=11, blank=True,
        help_text='DNI o RUC',
        verbose_name='Documento de Identidad')
    profession = models.CharField(max_length=1,
        help_text='Profesión', choices=PROFESSION_CHOICES,
        verbose_name='Profesión', blank=True)
    mobile = models.CharField(max_length=12, blank=True,
        help_text='Número de Teléfono Celular',
        verbose_name='Celular')
    phone = models.CharField(max_length=10, blank=True, null=True,
        help_text='Número de Teléfono Fijo o de Oficina',
        verbose_name='Teléfono')
    email = models.EmailField(max_length=50, blank=False,
        help_text='Correo Electrónico',
        verbose_name='Email')
    tuition = models.PositiveIntegerField(null=True, blank=True,
        help_text='Colegiatura',
        verbose_name='Colegiatura')
    secret_code = models.PositiveIntegerField(null=True, blank=True,
        help_text='Código Secreto de Arquitecto',
        verbose_name='Código Secreto de Arquitecto')
    address = models.CharField(max_length=200, blank=True, null=True,
        help_text='Dirección',
        verbose_name='Dirección')
    # is_signature_validated = models.BooleanField(blank=True,
    #     help_text='Marcado si la firma está validada por el CAP',
    #     verbose_name='Firma Validada')
    # signature = models.ImageField(
    #     upload_to=upload_signature, blank=True,
    #     help_text='Suba una imágen escaneada de su sello y firma, los cuales será utilizados como validación de las solicitudes que realice através del portal',
    #     verbose_name='Firma')
    area_interest = models.CharField(max_length=200, blank=True,
        help_text='areas de interes',
        verbose_name='areas de interes')
    institution = models.CharField(max_length=200, blank=True,
        help_text='Institucion',
        verbose_name='Institucion')
    photo = models.ImageField(
        upload_to=upload_photos, blank=True, null=True,
        help_text='Suba una fotografía en tamaño pasaporte o carnet',
        verbose_name='Fotografía')
    register_date_time = models.DateTimeField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    is_enabled = models.BooleanField(default=False, verbose_name='¿Esta habilitado?')
    penalty_fee = models.BooleanField(default=False, verbose_name='¿Tiene multas?')
    has_tutition = models.BooleanField(default=False, verbose_name='¿Es colegiado?')
    membership = models.ForeignKey(Membership, related_name='user_membership', 
                                        on_delete=models.SET_NULL,blank=True, null=True)
    
    suscripcion_foro = models.ManyToManyField(Foro, related_name="suscripcion_foro", blank=True) 
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    

    
    def __str__(self):
        return f'{self.names}  {self.first_surname}'
 
    class Meta:
        ordering = ['created']
         
    class Meta:  
        db_table = "member"

    class Meta:
        verbose_name_plural = 'Relacion de Miembros'

class UsagePolicies(models.Model):
    title = models.CharField(max_length = 200, blank=True)
    order = models.IntegerField(default=0, blank=True)
    description = models.TextField(verbose_name="Politicas de uso")
    member_policies = models.ManyToManyField(Member,
                                         related_name='member_policies', blank=True )
    validity_date_start = models.DateField(help_text='Fecha Inicio',verbose_name='Fecha Inicio')
    validity_date_finish = models.DateField(help_text='Fecha Fin',verbose_name='Fecha Fin')
    register_date_time = models.DateTimeField(auto_now_add=True,
                                                help_text='Fecha de Registro',
                                                verbose_name='Fecha de Registro')

    class Meta:
        verbose_name="Politicas de Uso"
        verbose_name_plural="Politicas de Uso"

    def __str__(self):
        return self.title

class Plan(models.Model):
    
    planame = models.CharField(max_length=200, blank=False,
        help_text='Nombre de Plan',
        verbose_name='Plan')      
    cost = models.DecimalField(max_digits = 10,decimal_places = 2)
    validity_date_start = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Inicio')
    validity_date_finish = models.DateField(
        blank=False, null=False, auto_now_add=False,
        help_text='Fecha',
        verbose_name='Fecha Fin')
    register_date_time = models.DateField(
        blank=False, null=False, auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    
    class Meta:
        verbose_name_plural = 'Planes de Suscripcion'

    def __str__(self):
        return self.planame 

class Order_payment(models.Model):
    
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE,
        help_text='Miembros', null=True, blank=True,
        verbose_name='Miembros', related_name='payment_order')
    names = models.CharField(max_length=50, blank=True,
        help_text='Nombres O Razón Social',
        verbose_name='Nombres')
    first_surname = models.CharField(max_length=50, blank=True,
        help_text='Apellido Paterno',
        verbose_name='Apellido Paterno')
    second_surname = models.CharField(max_length=50, blank=True,
        help_text='Apellido Materno',
        verbose_name='Apellido Materno')
    email = models.EmailField(max_length=50, blank=True, null=True,
        help_text='Correo Electrónico',
        verbose_name='Email')
    identity = models.CharField(max_length=11, blank=True,
        help_text='DNI o RUC',
        verbose_name='Documento de Identidad')
    paid = models.BooleanField(default=False)
    niubiz_id = models.CharField(max_length=150, blank=True)        
    pay_method = models.CharField(max_length=1,
        help_text='Metodo de Pago', choices=METODPAY_CHOICES,
        verbose_name='Metodo de Pago', blank=True)
    pay_import = models.DecimalField(max_digits = 10,decimal_places = 2,
        help_text='Importe Pagado',
        verbose_name='Importe Pagado')  
    validity_date_start = models.DateTimeField(
        blank=False, null=False,
        help_text='Fecha Inicio membresia',
        verbose_name='Fecha Inicio membresia')
    validity_date_finish = models.DateTimeField(
        blank=False, null=False,
        help_text='Fecha Fin membresia',
        verbose_name='Fecha Fin membresia')
    created= models.DateTimeField( auto_now_add=True,
        help_text='Fecha de Registro',
        verbose_name='Fecha de Registro')
    updated= models.DateTimeField( auto_now=True,
        help_text='Fecha de Modificacion del Registro',
        verbose_name='Fecha de Modificacion del Registro')
    class Meta:
        verbose_name = 'Ordenes de Pagos'
        verbose_name_plural = 'Ordenes de Pagos'
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.names} {self.first_surname} {self.second_surname}'

class NiubizTransaction(models.Model):
    order_pyment = models.OneToOneField(Order_payment, on_delete=models.CASCADE, null=True, blank=True, related_name="niubiz_transaction")
    ecoreTransactionUUID = models.CharField(verbose_name="Identificador de la transaccion niubiz", 
                                            blank=True, max_length=100)
    channel = models.CharField(verbose_name="Canal de registro", blank=True, max_length=100)
    signature = models.CharField(verbose_name="Codigo niubiz", blank=True, max_length=100)
    tokenId = models.CharField(verbose_name="Token formulario niubiz", blank=True, max_length=100)
    purchaseNumber = models.CharField(verbose_name="Numero de pedido", blank=True, max_length=100)
    amount = models.CharField(verbose_name="Importe de la transaccion", blank=True, max_length=100)
    installment = models.CharField(verbose_name="Numero de cuotas", blank=True, max_length=100)
    currency = models.CharField(verbose_name="Moneda",blank=True, max_length=100)
    authorizedAmount= models.CharField(verbose_name="Importe confirmado",blank=True, max_length=100)
    authorizationCode = models.CharField(verbose_name="Codigo de autorización",blank=True, max_length=100)
    traceNumber = models.CharField(verbose_name="Identificador de la orden de transaccion",blank=True, max_length=100)
    #transactionDate = models.DateField(verbose_name="Fecha de la transacion",blank=True)
    card = models.CharField(verbose_name="Numero de tarjeta",blank=True, max_length=16)
    action_description = models.CharField(verbose_name="Descripcion de la transaccion",blank=True, max_length=100)
    brand = models.CharField(verbose_name="Nombre de la tarjeta",blank=True, max_length=15)
    
    class Meta:
        verbose_name= "Transaccion Niubiz"
        verbose_name_plural = "Transaccion Niubiz"

    def __str__(self):
        return self.purchaseNumber
class UserToken(models.Model):
    token = models.UUIDField(primary_key=True, null=False, unique=True,
        default=uuid.uuid4, editable=False)
    user_profile = models.OneToOneField(
        Member, on_delete=models.CASCADE,
        help_text='Usuario', null=False,
        verbose_name='Usuario')

    class Meta:
        verbose_name_plural = 'Tokens'

    def get_confirm_link(self):
        print (self.token)
        #return reverse('sign_up', kwargs={'token': self.token})
        

    def get_password_reset_link(self):
        return reverse('password_reset_token', kwargs={'token': self.token})

"""

 * TABLAS NORMAS 
 

"""

"""
"Registartions
 Attributes of Registartions are registration_id,registration_user_id,registration_name, registration_type,registration_number, registration_date,registration_description"

"Posts :
 post_id,post_user_id,post_title,post_type, post_description"

"Replies :
 replies_id, replies_user_id,replies_title, replies_type,replies_description"

"Polls Entity : Attributes of Polls are poll_id,poll_name, pon_type, poll_description"
https://github.com/mdn/django-diy-blog/blob/master/blog/models.py
"""
