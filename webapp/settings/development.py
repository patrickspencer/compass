from .base import *

DEBUG = True

# TEMPLATES[1]['DEBUG'] = True

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, '..', 'tmp', 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compass_webapp_dev',
        'USER': 'compass_webapp',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DEVELOPMENT_APPS = [
        'django.contrib.admin',
        'debug_toolbar',
        'django_extensions',
        ]

INSTALLED_APPS += DEVELOPMENT_APPS

