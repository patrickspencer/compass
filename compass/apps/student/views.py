from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse, resolve


def student_home(request):
    current_url = resolve(request.path_info).url_name
    logged_in = request.user.is_authenticated()
    user_groups = request.user.groups.values_list('name',flat=True)
    view_name = resolve(request.path_info).url_name
    return render(request, 'student/base.html', {
        'user': request.user,
        'current_url': current_url,
        'logged_in': logged_in,
        'user_groups': type(list(user_groups)),
        'view_name_type': view_name,
    })

