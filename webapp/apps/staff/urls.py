from django.conf.urls import patterns, include, url
import apps.staff.views


# These urls are included in apps.core.urls
# so they are relative to /staff. For example
# admin_home_url is set to / but it's accesible
# at /staff/

urlpatterns = patterns('',
    url(r'^$', apps.staff.views.admin_view,
        name='admin_home_url'),
    url(r'new/$', apps.staff.views.users_new_view,
        name='users_new_url'),
)

