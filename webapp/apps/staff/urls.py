from django.conf.urls import include, url
import apps.staff.views

# These urls are included in apps.core.urls
# so they are relative to /staff. For example
# users_home is set to ^users$ but it's accessible
# at /staff/users/

urlpatterns = [
    url(r'^users$', apps.staff.views.Index.as_view(), name='users_home'),
    url(r'^users/create$', apps.staff.views.Create.as_view(), name='users_create'),
    url(r'^users/(?P<pk>[0-9]+)/delete$',
      apps.staff.views.Delete.as_view(), name='users_delete'),
    url(r'^users/(?P<pk>[0-9]+)/update$',
      apps.staff.views.Update.as_view(), name='users_update'),
]

