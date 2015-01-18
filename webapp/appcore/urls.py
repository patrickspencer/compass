from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
import appcore.views


urlpatterns = patterns('',
    url(r'^$', include('appstudent.urls')),
    url(r'^staff/$', include('appstaff.urls')),
    url(r'^login/$', appcore.views.login_view, name='login_url'),
    url(r'^logout/$', appcore.views.logout_view, name='logout_url'),
    url(r'^admin/', include(admin.site.urls), name='djadmin'),
)
