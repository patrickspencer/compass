from .base import *

DEBUG = True

# TEMPLATES[1]['DEBUG'] = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compass_webapp_dev',
        'USER': 'compass_webapp',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEVELOPMENT_APPS = [
        'debug_toolbar',
        ]

INSTALLED_APPS += DEVELOPMENT_APPS

