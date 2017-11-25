from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
import apps.core.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$',RedirectView.as_view(url='/student/problems/', permanent=False), name='index'),
    url(r'^student/', include('apps.student.urls', namespace='student')),
    url(r'^staff/', include('apps.staff.urls', namespace='staff')),
    url(r'^login/$', apps.core.views.Login.as_view(), name='login'),
    url(r'^logout/$', apps.core.views.Logout.as_view(), name='logout'),
    # url(r'^admin/', include(admin.site.urls), name='djadmin'),
]
