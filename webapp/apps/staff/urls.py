from django.conf.urls import patterns, include, url
import apps.staff.views


# These urls are included in apps.core.urls
# so they are relative to /admin. For example
# admin_home_url is set to / but it's accesible
# at /admin/

urlpatterns = patterns('',
    url(r'^$', apps.staff.views.admin_view,
        name='admin_home_url'),
)

