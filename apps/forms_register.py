from django import forms
from apps.models import Member
from membership.models import APIMember

class MemberCapForm(forms.Form):
    email = forms.EmailField(label='email',required=True ,
                            widget=forms.EmailInput(attrs={
                                'class': "form-control",
                                'placeholder' : 'correo@dominio.com'
                                }),
                                help_text='Ingresa el email',
                                )
    password1 = forms.CharField(label='password1',required=True ,
                        widget=forms.PasswordInput(attrs={
                                'class': "form-control",
                                'placeholder' : 'Ingresa una contraseña'
                                }),
                                help_text='Ingresa una contraseña correcta',
                                )
    password2 = forms.CharField(label='password2',required=True ,
                        widget=forms.PasswordInput(attrs={
                                'class': "form-control",
                                'placeholder' : 'Confirma la contraseña'
                                }),
                                help_text='Confirma la contraseña, ambas contraseñas deben ser iguales',
                                )
class MemberPremiumCapForm(forms.Form):
    email = forms.EmailField(label='email',required=True ,
                            widget=forms.EmailInput(attrs={
                                'class': "form-control",
                                'placeholder' : 'correo@dominio.com'
                                }),
                                help_text='Ingresa el email',
                                )
    password1 = forms.CharField(label='password1',required=True ,
                        widget=forms.PasswordInput(attrs={
                                'class': "form-control",
                                'placeholder' : 'Ingresa una contraseña'
                                }),
                                help_text='Ingresa una contraseña correcta',
                                )
    password2 = forms.CharField(label='password2',required=True ,
                        widget=forms.PasswordInput(attrs={
                                'class': "form-control",
                                'placeholder' : 'Confirma la contraseña'
                                }),
                                help_text='Confirma la contraseña, ambas contraseñas deben ser iguales',
                                )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        member = Member.objects.filter(email=email).exists()

        if member:
            print('error en el email')
            raise forms.ValidationError("Este email ya se encuentra registrado")
 
        else:
            exists_user = APIMember.objects.filter(email=email).exists()
            if exists_user :
                api_user = APIMember.objects.filter(email=email)[0]
                if not api_user.has_tutition or not api_user.is_enabled or api_user.penalty_fee:
                    raise forms.ValidationError(f"Estimado(a) {api_user.name_user} , No puedes acceder debido a que tienes alguna multa o no te encuentras habilitado, para mayor informacion por favor comunicate con el C.A.P.")
            else:
                raise forms.ValidationError('No eres un usuario agremiado, debes escoger un plan profesional para poder registrarte.')

        return email
                
    def clean_password1(self):
        password1 =self.data.get('password1')
        password2 =self.data.get('password2')
        
        if  len(str(password1)) < 8:
            print('error en la contraseña')
            print("eror passw 2", password2)
            
            raise forms.ValidationError("Esta contraseña es demasiado corta. Debe contener al menos 8 caracteres.")
        if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden deden ser iguales")

        return password1

class ExternalUserForm(forms.Form):

        names = forms.CharField(label='Nombres',required=True ,
                            widget=forms.TextInput(attrs={
                                'class': "form-control",
                                'placeholder' : ''
                                }),
                                help_text='Ingresa tu nombre',)
        first_surname = forms.CharField(label='Primer Apellido',required=True ,
                                widget=forms.TextInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : ''
                                        }),
                                        help_text='Ingresa Apellido paterno',)
        second_surname = forms.CharField(label='Segundo Apellido',required=True ,
                                widget=forms.TextInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : ''
                                        }),
                                        help_text='Ingresa Apellido materno',)
        identity = forms.IntegerField(label='Documento Nacional de Identidad',required=True ,
                                widget=forms.NumberInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : ''
                                        }),
                                        help_text='Ingresa tu Documento Nacional de Identidad',)
        #person_type = forms.IntegerField()
        mobile = forms.IntegerField(label='Teléfono Celular',required=True ,
                                widget=forms.NumberInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : ''
                                        }),
                                        help_text='Ingresa tu numero de telefono celular',)
        phone = forms.IntegerField(label='Teléfono Fijo' ,required=False,
                                widget=forms.NumberInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : ''
                                        }),
                                        help_text='Ingresa tu numero de telefono fijo',)
        email = forms.EmailField(label='Correo Electrónico:',required=True ,
                                widget=forms.EmailInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : 'correo@dominio.com'
                                        }),
                                        help_text='Ingresa tu eamil',)
        address = forms.CharField(label='Dirección' , required=False,
                                widget=forms.TextInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : ''
                                        }),
                                        help_text='Ingresa tu direccion',)
        #person_type = forms.IntegerField()

        password1 = forms.CharField(label='password1',required=True ,
                                widget=forms.PasswordInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : 'Ingresa una contraseña'
                                        }),
                                        help_text='Ingresa una contraseña correcta',
                                        )
        password2 = forms.CharField(label='password2', required=True ,
                                widget=forms.PasswordInput(attrs={
                                        'class': "form-control",
                                        'placeholder' : 'Confirma la contraseña'
                                        }),
                                        help_text='Confirma la contraseña, ambas contraseñas deben ser iguales',
                                        )

        def clean_email(self):
            email = self.cleaned_data['email']
            member = Member.objects.filter(email=email).exists()

            if member:
                print('error en el email')
                raise forms.ValidationError("Este email ya se encuentra registrado")
            return email

        def clean_identity(self):
            identity = self.cleaned_data['identity']
            
            if  len(str(identity)) < 8:
                print('error en el dni')
                raise forms.ValidationError("Ingrese un número de DNI válido")
            
            return identity
                    

        def clean_mobile(self):
            mobile = self.cleaned_data['mobile']
            
            if  len(str(mobile)) < 9:
                print('error en el dni')
                raise forms.ValidationError("Ingrese un número de celular válido")
            
            return mobile

        def clean_password1(self):
            password1 =self.data.get('password1')
            password2 =self.data.get('password2')
            
            if  len(str(password1)) < 8:
                print('error en la contraseña')
                print("eror passw 2", password2)
                
                raise forms.ValidationError("Esta contraseña es demasiado corta. Debe contener al menos 8 caracteres.")
            if password1 != password2:
                    raise forms.ValidationError("Las contraseñas no coinciden deden ser iguales")

            return password1