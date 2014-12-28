from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, resolve
from django.contrib.auth import authenticate, login, logout
from backend.forms.login import LoginForm

def home_view(request):
    current_url = resolve(request.path_info).url_name
    logged_in = request.user.is_authenticated()
    user_groups = request.user.groups.values_list('name',flat=True)
    view_name = resolve(request.path_info).url_name
    return render(request, 'student/base.jinja', {
        'user': request.user,
        'current_url': current_url,
        'logged_in': logged_in,
        'user_groups': type(list(user_groups)),
        'view_name_type': view_name,
    })

def admin_view(request):
    return render(request, 'admin/base.jinja', {
        'user': request.user,
        'groups': request.user.groups.get(),
    })

def secret(request):
    return render(request, 'student/base.jinja', {
        'message': 'This page is a secret',
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass

    form = LoginForm
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

