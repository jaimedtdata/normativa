from django import forms
from django.contrib.auth.forms import AuthenticationForm
from normas.models import Categories_Normas,Areas_Normas,Subcategories_Normas,Location_Normas
from .models import Plan, Member
from foro.models import Coments_foro



USER_CONTROL = {'class': 'form-control', 'placeholder':'Usuario/CAP'}
PASSWORD_CONTROL = {'class': 'form-control', 'placeholder':'Contraseña', 'type':'password'}



FORM_CONTROL = {'class': 'form-control'}
SELECT2_CONTROL = {'class': 'form-control select2', 'style':'width:100% !important;'}

TEXTAREA_CONTROL = {
    'class': 'form-control',
    'rows': '4'
}
DIA_CONTROL = {
    'class': 'form-control',
    'min':1,
    'max':30,
}
YEAR_CONTROL = {
    'class': 'form-control',
    'min':2000,
    'max':2020,
}
CANTIDAD_CONTROL = {
    'class': 'form-control',
    'min':0,
    'max':100,
}
DECIMAL_CONTROL = {
    'class': 'form-control',
    'step':.1,
    'min':0,
}
NUMBER_NONE_CONTROL = {'class': 'form-control none_arrows',}
DATE_CONTROL = {
    'class': 'form-control datepicker-here',
    'data-language':'es'
}
DATE_MONTH_CONTROL = {
    'class': 'form-control datepicker-here',
    'data-language':'es',
    'data-min-view':"months",
    'data-view':"months",
    'data-date-format':"MM",
}
DATE_DAY_CONTROL = {
    'class': 'form-control datepicker-here',
    'data-language':'es',
    'data-date-format':"dd",
}
TIME_CONTROL = {
    'class': 'form-control timepicker',
    'disable':'false'
}

MUNI_CHOICES = (
    ('0','Elija una opción'),
    ('1','Cercado de Lima'),
    ('3','Ate'),
    ('4','Barranci'),
    ('5','Breña'),
    ('7','Comas'),
    ('9','Chorrillos'),
    ('10','El Agustino'),
    ('11','Jesús María'),
    ('12','La Molina'),
    ('13','La Victoria'),
    ('14','Lince'),
    ('17','Magdalena del Mar'),
    ('18','Miraflores'),
    ('21','Pueblo Libre'),
    ('22','Puente Piedra'),
    ('25','Rimac'),
    ('27','San Isidro'),
    ('28','Independencia'),
    ('29','San Juan de Miraflores'),
    ('30','San Luis'),
    ('31','San Martin de Porres'),
    ('32','San Miguel'),
    ('33','Santiago de Surco'),
    ('34','Surquillo'),
    ('35','Villa María del Triunfo'),
    ('36','San Juan de Lurigancho'),
    ('38','Santa Rosa'),
    ('39','Los Olivos'),
    ('41','San Borja'),
    ('42','Villa El Savador'),
    ('43', 'Santa Anit'),
)

PROVINCE_CHOICES = (
    ('1','Lima'),
    ('2','Barranca'),
    ('3','Cajatambo'),
    ('4','Canta'),
    ('5','Cañete'),
    ('6','Huaral'),
    ('7','Huarochirí'),
    ('8','Huaura'),
    ('9','Oyón'),
    ('10','Yauyos'),
)

CONDICION_CHOICES = (
    ('0', '---'),
    ('1', 'T'),
    ('2', 'TC'),
    ('3', 'S'),
    ('4', 'A'),
)

YEAR_CHOICES = (
    ('0',''),
    ('1','2020'),
    ('2','2019'),
    ('3','2018'),
    ('4','2017'),
    ('5','2016'),
    ('6','2015'),
    ('7','2014'),
    ('8','2013'),
    ('9','2012'),
    ('10','2011'),
    ('11','2010'),
)

TXT_FIELD = forms.Field(required=False, widget= forms.TextInput(attrs=FORM_CONTROL))
NUM_FIELD = forms.Field(required=False, widget= forms.NumberInput(attrs=CANTIDAD_CONTROL))
DECIMAL_FIELD = forms.Field(required=False, widget= forms.NumberInput(attrs=DECIMAL_CONTROL))
DATE_FIELD = forms.Field(required=False, widget= forms.TextInput(attrs=DATE_CONTROL))
TIME_FIELD = forms.Field(required=False, widget= forms.TextInput(attrs=TIME_CONTROL))
TXTAREA_FIELD = forms.Field(required=False, widget= forms.Textarea(attrs=TEXTAREA_CONTROL))

FORM_CONTROL = {'class': 'form-control'}
FORM_CONTROL_UPPER = {'class': 'form-control upper-case'}
TEXTAREA_CONTROL = {'class': 'form-control','rows': '4'}
TEXTAREA_UPPER_CONTROL = {'class': 'form-control upper-case','rows': '4'}
FORM_CONTROL_UPPER_N_LETTERS = {'class': 'form-control upper-case just-letters'}
FORM_CONTROL_DISABLED = {'class': 'form-control', 'disabled':''}
FORM_CONTROL_READONLY = {'class': 'form-control', 'readOnly':'true'}
NO_DISABLED_CONTROL = {'class': 'form-control no-disabled-case'}
 
DNI_CONTROL = {'class': 'form-control dni-case'}
USE_TYPE_CONTROL = {'class': 'form-control use_type_change'}
USE_AREA_CONTROL = {'class': 'form-control use_area_change','min':0}

PASSWORD_CONTROL = {'class': 'form-control', 'placeholder':'Contraseña', 'type':'password'}
PHONE_CONTROL = {'class': 'form-control','placeholder':'Ejemplo: 01202120'}
CELLPHONE_CONTROL = {'class': 'form-control cellphone-case','min':900000000, 'max':999999999}
EMAIL_CONTROL = {'class': 'form-control'}
EMAIL_PH_CONTROL = {'class': 'form-control', 'placeholder':'Correo Electrónico'}

#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Forms
#https://stackoverflow.com/questions/2303268/djangos-forms-form-vs-forms-modelform
#https://djangobook.com/mdj2-django-forms/

class ExternalRegisterForm(forms.ModelForm):
        class Meta:
                model = Member
                exclude = ('user','full_name','roles')
                fields = [
                    'names',
                    'first_surname',
                    'second_surname',
                    'identity',
                    'person_type',
                    'mobile',
                    'phone',
                    'email',
                    'address',
                    'profession',
                    'tuition',
                    'secret_code',
                ]
                widgets = {
                    'names': forms.TextInput(attrs=FORM_CONTROL_UPPER_N_LETTERS),
                    'first_surname': forms.TextInput(attrs=FORM_CONTROL_UPPER_N_LETTERS),
                    'second_surname': forms.TextInput(attrs=FORM_CONTROL_UPPER_N_LETTERS),
                    'identity': forms.NumberInput(attrs=DNI_CONTROL),
                    'mobile': forms.NumberInput(attrs=CELLPHONE_CONTROL),
                    'phone': forms.NumberInput(attrs=PHONE_CONTROL),
                    'email': forms.TextInput(attrs=EMAIL_CONTROL),
                    'address': forms.TextInput(attrs=FORM_CONTROL_UPPER),
                    'profession': forms.Select(attrs=SELECT2_CONTROL),
                    'tuition': forms.NumberInput(attrs=FORM_CONTROL),
                    'secret_code': forms.NumberInput(attrs=FORM_CONTROL),
                    'person_type': forms.Select(attrs=SELECT2_CONTROL),
                }

                def clean(self):
                    cleaned_data = super().clean()
                    email = cleaned_data.get("email")
                    identity = cleaned_data.get("identity")
                    person_type = cleaned_data.get("person_type")
                    address = cleaned_data.get("address")

                    profiles = Member.objects.filter(email=email)
                    if profiles:
                        self.add_error('email', "Este correo electrónico ya se encuentra registrado")
                    if  len(identity) != 8 and person_type == 'N':
                        self.add_error('identity', "Ingrese un número de DNI válido")
                    if  len(identity) != 11 and person_type == 'J':
                        self.add_error('identity', "Ingrese un número de RUC válido")
                    if  address == '' and person_type == 'J':
                        self.add_error('address', "Proporcione una dirección fiscal")
                    return cleaned_data
        


class CommentForm(forms.ModelForm):

    class Meta:
          model = Coments_foro
          fields = '__all__'
          widgets = {
                'coments': forms.TextInput(attrs=FORM_CONTROL),
            }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(USER_CONTROL)
        self.fields['password'].widget.attrs.update(PASSWORD_CONTROL)



class PlanForm(forms.ModelForm):
    #planame = forms.Field(required=False,label='Nombre Plan:',widget=forms.TextInput(attrs=FORM_CONTROL))
    #cost = forms.Field(required=False,label='costo:',widget=forms.NumberInput(attrs=DECIMAL_CONTROL))
    #required_css_class = 'required'
    class Meta:
          model = Plan
          fields = '__all__'
          widgets = {
                'planame': forms.TextInput(attrs=FORM_CONTROL),
                'cost': forms.NumberInput(attrs=DECIMAL_CONTROL),
            }
    #para model form si puede ir instance 
    # class Meta:
    #       model = Plan
    #       fields = ['planame', 'cost']



    # muni = forms.ChoiceField(
    # 	required=False,
    # 	label = 'Municipalidad:',
    # 	widget= forms.Select(attrs=FORM_CONTROL),
    # 	choices = MUNI_CHOICES
    # )

class LiquidForm(forms.Form):
    muni = forms.ChoiceField(
        label = 'Municipalidad:',
        widget= forms.Select(attrs=FORM_CONTROL),
        choices = MUNI_CHOICES
    )
    dia = forms.Field(label='Día:',widget= forms.TextInput(attrs=DATE_DAY_CONTROL))
    mes = forms.Field(label='Mes:',widget= forms.TextInput(attrs=DATE_MONTH_CONTROL))
    num = NUM_FIELD
    decimal = DECIMAL_FIELD
    total_cant = forms.IntegerField(
        label = '',
        widget= forms.NumberInput(attrs=CANTIDAD_CONTROL),
    )
    obs = forms.Field(label = 'Observaciones Generales:',widget= forms.Textarea(attrs=TEXTAREA_CONTROL))

class SessionForm(forms.Form):
    names = forms.Field(label = 'Nombres:',widget= forms.TextInput(attrs=FORM_CONTROL))
    ncap = forms.Field(label = 'N° CAP:',widget= forms.TextInput(attrs=FORM_CONTROL))
    condicion = forms.ChoiceField(
        label = 'Condición:',
        widget= forms.Select(attrs=FORM_CONTROL),
        choices = CONDICION_CHOICES
    )
    nsesions = forms.Field(label = 'Cantidad de Sesiones:',widget= forms.TextInput(attrs=FORM_CONTROL))

class ArquitectForm(forms.Form):
    name = forms.Field(label='Nombre:',widget=forms.TextInput(attrs=FORM_CONTROL))
    cargo = forms.Field(label='Cargo:',widget=forms.TextInput(attrs=FORM_CONTROL))

class EntrevistaInForm(forms.Form):
    txt = forms.Field(widget=forms.TextInput(attrs=FORM_CONTROL))
    date = DATE_FIELD

SessionFormset = forms.formset_factory(SessionForm, can_delete=True)
ArquitectFormset = forms.formset_factory(ArquitectForm, can_delete=True)
EntrevistaFormset = forms.formset_factory(EntrevistaInForm, can_delete=True)

class EntrevistaForm(forms.Form):
    muni = forms.ChoiceField(widget= forms.Select(attrs=FORM_CONTROL), choices=MUNI_CHOICES)
    mes = forms.Field(widget= forms.TextInput(attrs=DATE_MONTH_CONTROL))
    year = forms.ChoiceField(widget= forms.Select(attrs=FORM_CONTROL), choices=YEAR_CHOICES)

class ComisionForm(forms.Form):
    muni = forms.ChoiceField(
        label = '1.	Sede de la Comisión Técnica de Edificaciones de la Municipalidad Distrital (o Provincial) de:',
        widget= forms.Select(attrs=FORM_CONTROL),
        choices = MUNI_CHOICES
    )
    direccion = forms.Field(label = 'Dirección:',widget= forms.TextInput(attrs=FORM_CONTROL))
    telef = forms.Field(label = 'Teléfono(s):',widget= forms.TextInput(attrs=FORM_CONTROL))
    email = forms.Field(label = 'E-mail:',widget= forms.TextInput(attrs=FORM_CONTROL))
    alcalde = forms.Field(label = '2. Alcalde',widget= forms.TextInput(attrs=FORM_CONTROL))
    prof = forms.Field(label = 'Profesión:',widget= forms.TextInput(attrs=FORM_CONTROL))
    regulador = forms.Field(
        label = '3. Regidor de la Comisión de desarrollo Urbano',widget= forms.TextInput(attrs=FORM_CONTROL))
    gerente = forms.Field(
        label = '4. Gerente (o Director) de Desarrollo Urbano',widget= forms.TextInput(attrs=FORM_CONTROL))
    chbx = forms.BooleanField(widget= forms.CheckboxInput(attrs=FORM_CONTROL))
    cap = forms.Field(widget= forms.TextInput(attrs=FORM_CONTROL))
    obs = TXTAREA_FIELD
    txt = TXT_FIELD
    date = DATE_FIELD
    time = TIME_FIELD


from apps.choices import (RULES_TYPES,LOCATIONS_CHOICES,)

class RulesForm(forms.Form):

    # Tipo Normativa
    #Error
    #SECTIONS_CHOICES =  list(Subcategories_Normas.objects.values_list('id', 'subcategory_name'))
    
    # Uso Categoria
    #RULES_TYPES =  list(Categories_Normas.objects.values_list('id', 'category_name'))
    RULES_TYPES =  (
     ('','-------- Todos --------'),
     ('','Hospedaje'),
     ('','Educación'),
     ('','Salud'),
    )


    #LOCATIONS_CHOICES =  list(Location_Normas.objects.values_list('id', 'Location_name'))
    
    LOCATIONS_CHOICES =  (
     ('','-------- Todos --------'),
     ('','Hospedaje'),
     ('','Educación'),
     ('','Salud'),
    )
    SECTIONS_CHOICES = (
     ('','-------- Todos --------'),
     ('','Hospedaje'),
     ('','Educación'),
     ('','Salud'),
    )
    
    sections = forms.ChoiceField(required=False, widget= forms.Select(attrs=SELECT2_CONTROL), choices=SECTIONS_CHOICES)
    rule_type = forms.ChoiceField(required=False, widget= forms.Select(attrs=SELECT2_CONTROL), choices=RULES_TYPES)
    locations = forms.ChoiceField(required=False, widget= forms.Select(attrs=SELECT2_CONTROL), choices=LOCATIONS_CHOICES)
    f_in = DATE_FIELD
    f_out = DATE_FIELD
    year = forms.ChoiceField(required=False, widget= forms.Select(attrs=FORM_CONTROL), choices=YEAR_CHOICES)
    title = TXT_FIELD

#johao

#end