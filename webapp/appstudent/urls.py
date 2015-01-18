from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import appstudent.views


# These urls are included in compass.urls
# so they are relative to /admin. For example
# student_home_url is set to / but it's accessible
# at /s/
urlpatterns = patterns('',
    url(r'^$', appstudent.views.student_home,
        name='home_url'),
)

