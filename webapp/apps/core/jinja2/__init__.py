from __future__ import absolute_import  # Python 2 only
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from apps.core.jinja2 import filters


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    env.filters.update({
        'strftime': filters.strftime,
        'roundfloat': filters.roundfloat,
    })
    return env
