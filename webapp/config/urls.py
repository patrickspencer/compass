from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
import apps.core.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^', include('apps.student.urls')),
    url(r'^staff/', include('apps.staff.urls', namespace='staff')),
    url(r'^login/$', apps.core.views.login_view, name='login'),
    url(r'^logout/$', apps.core.views.logout_view, name='logout'),
    # url(r'^admin/', include(admin.site.urls), name='djadmin'),
]