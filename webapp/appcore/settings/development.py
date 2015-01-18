from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'tmp', 'db.sqlite3'),
    }
}

DEVELOPMENT_APPS = [
        'django.contrib.admin',
        'debug_toolbar',
        ]

INSTALLED_APPS += DEVELOPMENT_APPS

