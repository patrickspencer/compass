import re

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import resolve
from django.shortcuts import redirect
from apps.core.views import login_view

"""
This script from
http://stackoverflow.com/questions/2164069/best-way-to-make-djangos-login-required-the-default
"""

class RequireLoginMiddleware(object):
    """
    Middleware component that wraps the login_required decorator around
    matching URL patterns.
    """

    def __init__(self):
        self.required = re.compile(r'/admin/(.*)$')

    def process_view(self, request, view_func, view_args, view_kwargs):

        # view_name is the url_name of the ResolverMatch. It's the name given
        # to the url pattern of the current url the page is viewing
        view_name = resolve(request.path_info).url_name
        user = request.user

        if user is not None:
            logged_in = user.is_authenticated()
            user_groups = list(user.groups.values_list('name',flat=True))

            if not logged_in and view_name != 'login_url':
                return login_required(view_func)(request, *view_args, **view_kwargs)

            # if logged_in:
            #     is_protected = self.required.match(request.path)
            #
            #     if is_protected and ('instructor' not in user_groups):
            #         return redirect('/')
            #
            #     if not is_protected and ('instructor' in user_groups):
            #
            #         if view_name == 'logout_url':
            #             return None
            #
            #         return redirect('/admin')


        # Explicitly return None for all non-matching requests
        return None
