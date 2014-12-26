from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from backend.forms.login import LoginForm

def home(request):
    if request.user.is_authenticated():
        other_message = 'you are logged in'
    else:
        other_message = 'go away'

    return render(request, 'student/base.jinja', {
        'user': request.user,
        'groups': request.user.groups.get(),
        'other_message': other_message,
    })

def secret(request):
    return render(request, 'base.html', {
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

