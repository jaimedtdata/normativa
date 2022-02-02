from datetime import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader
from django.urls import reverse,reverse_lazy
from django.core.mail import EmailMessage
from django.core.files.base import ContentFile
from cap import settings

FROM_EMAIL = 'Colegio de Arquitectos <{}>'.format(settings.EMAIL_HOST_USER)

def send_confirm_account(request, link, email):
	context = {
		'title': 'Verificación de correo electrónico',
		'message': 'Confirmación de Correo Electrónico',
		'link': link,
		'request':request,
	}
	from_email = FROM_EMAIL
	print ('from_email:',from_email,[email])

	html_message = loader.render_to_string('confirm_account.html', context)
	return send_mail(context['title'], context['message'], 
		from_email, [email], fail_silently=False, 
		html_message=html_message)

def send_success_sign_up(request, profile):
	context = {
		'title': 'Registro Exitoso',
		'message': 'Registro Exitoso',
		'profile': profile,
		'request':request,
	}
	from_email = FROM_EMAIL
	html_message = loader.render_to_string('success_sign_up.html', context)
	return send_mail(context['title'], context['message'], 
		from_email, [profile.email], 
		fail_silently=False, html_message=html_message)

def send_password_reset(request, link, email):
	context = {
		'title': 'Recupera tu Contraseña',
		'message': 'Recupera tu Contraseña',
		'link': link,
		'request':request,
	}
	from_email = FROM_EMAIL
	html_message = loader.render_to_string('password_reset.html', context)
	return send_mail(context['title'], context['message'], 
		from_email, [email], fail_silently=False, 
		html_message=html_message)

def send_success_password_reset(request, profile):
	context = {
		'title': 'Credenciales Actualizadas',
		'message': 'Credenciales Actualizadas',
		'profile': profile,
		'request':request,
	}
	from_email = FROM_EMAIL
	html_message = loader.render_to_string('success_password_reset.html', context)
	return send_mail(context['title'], context['message'], from_email, [profile.email], fail_silently=False, html_message=html_message)