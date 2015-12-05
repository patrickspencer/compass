from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import apps.student.views


# These urls are included in apps.core.urls
# so they are relative to /admin. For example
# student_home_url is set to / but it's accessible
# at /s/
urlpatterns = [
    url(r'^$', apps.student.views.student_home,
        name='home_url'),
]

