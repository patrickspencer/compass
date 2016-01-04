"""
WSGI config for compass project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/var/compass/webapp')
sys.path.append('/virtualenv/compass/lib/python2.7/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

