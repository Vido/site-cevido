"""
Django settings for cevido project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ir_9$lk-@*o4xfji)0w8g68yps!+ox968p8z$amanhbuia3g1m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

PRODUCTION = 'PRODUCTION' in os.listdir(BASE_DIR)

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'south',
    'mptt',
    'easy_thumbnails',
    'filer',
    'newsletter',
    'real_estate',
    'filter',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cevido.urls'

if PRODUCTION:
    WSGI_APPLICATION = 'cevido.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/static/'
if PRODUCTION:
    STATIC_URL = 'http://static.cevido.com.br/'
else:
    STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR + '/static/',
)

MEDIA_ROOT = BASE_DIR + '/media/'
if PRODUCTION:
    MEDIA_URL = 'http://media.cevido.com.br/'
else:
    MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/'
)
