from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Member
from membership.models import APIMember

class MemberCAPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    cap = serializers.IntegerField()
    password1 = serializers.CharField( style={'input_type': 'password'})
    password2 = serializers.CharField( style={'input_type': 'password'})
    #validar que el email sea el que esta en erp

    def validate_email(self, value):
        member = APIMember.objects.filter(email=value).exists()
        if  not member :
            raise ValidationError("Tu email debe ser igual al que tienes registrado en el CAP.")
        return value

    def validate(self, data):
        
        if len(data['password1']) < 8 :
            raise ValidationError('La contraseña es muy corta')

        if  data['password1'] != data['password2']:
            raise ValidationError('Las contraseñas no coinciden, deben ser iguales')
        return data

    

class MemberExternalSerializer(serializers.Serializer):
    names = serializers.CharField()
    first_surname = serializers.CharField()
    second_surname = serializers.CharField()
    identity = serializers.IntegerField()
    mobile = serializers.IntegerField()
    phone = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.EmailField()
    address = serializers.CharField(required=False, allow_null=True)

    password1 = serializers.CharField( style={'input_type': 'password'})
    password2 = serializers.CharField( style={'input_type': 'password'})

    def validate(self, data):
        # email_form = data['email']
        # member = Member.objects.filter(email=email_form).exists()
        # if  member :
        #     raise ValidationError("Este email ya se encuentra registrado.")
        
        if len(data['password1']) < 8 :
            raise ValidationError('La contraseña es muy corta')

        if  data['password1'] != data['password2']:
            raise ValidationError('Las contraseñas no coinciden, deben ser iguales')
        return data
    
    def validate_email(self, value):
        member = Member.objects.filter(email=value).exists()
        if  member :
            raise ValidationError("Este email ya se encuentra registrado.")
        return value
    
    def validate_mobile(self, value):
        if len(str(value))<9 :
            raise ValidationError("El numero de celular debe tener 9 digitos.")
        return value


class ErpSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIMember
        #fields = '__all__'
        exclude = ['created', 'updated']