from django import forms

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