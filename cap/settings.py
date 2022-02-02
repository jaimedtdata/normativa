from pathlib import Path
import dj_database_url
from django.urls import reverse_lazy
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'qrh*e^+4h@0j1zi_hc2knz5mx4ifq5*#3k-+dvf=2u$9%j@t43'

DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = ['*']

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_extensions',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'apps',
    'foro',
    'normas',
    'bus_normativa.apps.BusNormativaConfig'

)

# por Default agrega id automatico
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cap.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bdnormativa',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False
LOGIN_REDIRECT_URL = reverse_lazy('home')
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 's3'


#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    '/static/',
#]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#media
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jaimemarston@gmail.com'
EMAIL_HOST_PASSWORD = '42088985jrmm$$$'


# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# EMAIL_USE_LOCALTIME = config('EMAIL_USE_LOCALTIME', cast=bool)



# # Space AWS
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = config('AWS_LOCATION')

# activar iframe
# X_FRAME_OPTIONS = 'ALLOWALL'

# XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']# Configure Django App for Heroku.
