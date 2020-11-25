import os
from os.path import join
from sys import path
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)))))

path.append(join(BASE_DIR, 'server', 'src', 'apps'))


##################################################################
# API, URL
##################################################################

SITE_ID = 1

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
GEOAPIFY_STATIC_MAPS_API_KEY = os.getenv('GEOAPIFY_STATIC_MAPS_API_KEY')
DEFAULT_COORDINATES =  {'latitude':"56.0183900", 'longitude':"92.8671700"}
SECRET_KEY = '05o!hxym4rzido09o0^ms59l8j28=ijlf&5wsl!+i+vm_5q!!+'

ROOT_URLCONF = 'main.urls'
LOGIN_REDIRECT_URL = '/place-list'
LANDING_URL = '/'

ALLOWED_HOSTS = []
DEBUG = True

##################################################################
# Application definition
##################################################################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Django Applications
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django_extensions',
    'leaflet',

    # Project Applications
    'users.apps.UsersConfig',
    'places.apps.PlacesConfig',
)

##################################################################
# Templates, middleware settings
##################################################################

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'server', 'templates')],
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

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'wsgi.application'


##################################################################
# Databases settings (with docker)
##################################################################

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


##################################################################
# Locale
##################################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


##################################################################
# Static, Media
##################################################################

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'server', 'assets'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
