from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
import compass.views


# These urls are included in compass.urls
# so they are relative to /admin. For example
# admin_home_url is set to / but it's accesible
# at /admin/
urlpatterns = patterns('',
    url(r'^$', include('compass.apps.student.urls')),
    url(r'^staff/$', include('compass.apps.staff.urls')),
    url(r'^login/$', compass.views.login_view, name='login_url'),
    url(r'^logout/$', compass.views.logout_view, name='logout_url'),
    url(r'^admin/', include(admin.site.urls), name='djadmin'),
)
