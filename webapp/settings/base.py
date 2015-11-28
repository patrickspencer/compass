"""
Django settings for compass project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ca)pz=8)i47*e@e@2#z8wbhrofw39nd^y%xqi+9k9nqa1-)*6@'

ALLOWED_HOSTS = []

# Application definition

PREREQ_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'apps.core',
    'apps.staff',
    'apps.student',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.siteaccess.RequireLoginMiddleware',
]

ROOT_URLCONF = 'apps.core.urls'

WSGI_APPLICATION = 'apps.core.wsgi.application'

AUTH_PROFILE_MODULE = 'apps.core.UserProfile'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'assets', 'dist'),
        )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# this should be a blank directory where the 'collectstatic' command
# can relocate static files found in STATICFILES_DIRS
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# print("STATIC_ROOT:" + STATIC_ROOT)


TEMPLATES = [
    {
        'BACKEND': 'apps.core.jinja2.Jinja2Backend.Jinja2Backend',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        # 'DEBUG': True,
        'APP_DIRS': True,
        'OPTIONS': {'environment': 'apps.core.jinja2.environment'},
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'dj_templates')],
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


LOGIN_URL = '/login/'
