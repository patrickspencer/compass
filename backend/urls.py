from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import backend.views, django

urlpatterns = patterns('',
    url(r'^$', backend.views.home_view, name='home_url'),
    url(r'^secret/', backend.views.secret),
    url(r'^admin/$', backend.views.admin_view),
    url(r'^login/$', backend.views.login_view, name='login_url'),
    url(r'^logout/$', backend.views.logout_view, name='logout'),
    url(r'^djadmin/', include(admin.site.urls)),
)
