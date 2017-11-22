from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import apps.student.views


# These urls are included in apps.core.urls
# so they are relative to /student. For example
# student_home_url is set to / but it's accessible
# at /student/
urlpatterns = [
    url(r'^problems/$', apps.student.views.ProblemsIndex.as_view(), name='problems_index'),
    url(r'^problems/(?P<problem_id>[0-9]+)/$',
        apps.student.views.ProblemsShow.as_view(), name='problems_show'),
    url(r'^answers/update/$',
        apps.student.views.AnswerUpdate.as_view(), name='answers_update'),
]

