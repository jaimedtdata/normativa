from pathlib import Path
import dj_database_url
from django.urls import reverse_lazy
import os

##variables de entorno
import os
from dotenv import load_dotenv
load_dotenv()

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
    'django.contrib.postgres',
    'membership.apps.MembershipConfig',
    'rest_framework',
    'django_filters',
    'crispy_forms',
    'corsheaders',
)

LOCAL_APPS = (
    'apps',
    'foro',
    'normas',
    'bus_normativa.apps.BusNormativaConfig',
)

CRISPY_TEMPLATE_PACK = "bootstrap4"
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
LOGIN_URL = 'login'
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
    'corsheaders.middleware.CorsMiddleware',
    'apps.middleware.CheckMembership',
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
                'membership.context_processors.membership_type',
            ],
        },
    },
]

WSGI_APPLICATION = 'cap.wsgi.application'

# CORS_ALLOWED_ORIGINS = [
#     "https://apisandbox.vnforappstest.com",
#     "https://static-content-qas.vnforapps.com",
    
# ]

CORS_ORIGIN_ALLOW_ALL = True    #permitir acceder desde todos los dominios

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd4ot3mt28rcjob',
#         'USER': 'djmdailubuffcs',
#         'PASSWORD': '527d79120ffbcbba4dfd28b6a112541d902db70178ccdaf3468b547d6ac17cfc',
#         'HOST': 'ec2-44-192-245-97.compute-1.amazonaws.com',
#         'PORT': 5432,
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bdnormativa',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'apps.authentication.EmailAuthBackend',
]

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = False

LOGIN_REDIRECT_URL = reverse_lazy('home')

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#media
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

USERNAME_NIUBIZ = os.getenv('USERNAME_NIUBIZ')
PASSWORD_NIUBIZ = os.getenv('PASSWORD_NIUBIZ')
COMERCIAL_ID = os.getenv('COMERCIAL_ID')

CART_SESSION_ID = 'cart'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'jaimemarston@gmail.com'
# EMAIL_HOST_PASSWORD = '42088985jrmm$$$'


# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# EMAIL_USE_LOCALTIME = config('EMAIL_USE_LOCALTIME', cast=bool)



# # Space AWS
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = os.getenv('AWS_LOCATION')

# activar iframe
X_FRAME_OPTIONS = 'ALLOWALL'

# XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']# Configure Django App for Heroku.
