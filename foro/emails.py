from datetime import datetime
from django.core.mail import send_mail
from django.template import loader
from cap import settings
import threading

FROM_EMAIL = 'Colegio de Arquitectos <{}>'.format(settings.EMAIL_HOST_USER)

def send_email_suscription(request, emails):
	context = {
		'title': 'Notificación de suscripción',
		'message': 'Alguien hizo un comentario.',
		#'link': link,
		'request':request,
	}
	from_email = FROM_EMAIL
	print ('from_email:', from_email, emails)

	html_message = loader.render_to_string('email_foro_suscription.html', context)

	send_mail(
        context['title'], 
        context['message'], 
		from_email, 
        emails, 
        fail_silently=False, 
		html_message=html_message
    )

def async_send_email_suscription(request, emails):
    user = request.user

    thread = threading.Thread(target=send_email_suscription(request, emails), 
        args=(user,))
    thread.start()