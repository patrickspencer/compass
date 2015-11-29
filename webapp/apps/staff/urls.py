from django.conf.urls import patterns, include, url
import apps.staff.views

# These urls are included in apps.core.urls
# so they are relative to /staff. For example
# admin_home_url is set to / but it's accesible
# at /staff/

urlpatterns = [
    url(r'^users/$', apps.staff.views.index_view, name='index_url'),
    url(r'^users/new/$', apps.staff.views.users_new_view, name='users_new_url'),
]

