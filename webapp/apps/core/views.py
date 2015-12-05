from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.core.forms.login import LoginForm
from django.template.context_processors import csrf


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
            print("The username and password were incorrect.")
            form = LoginForm({'username': username, 'password': password})
    else:
        user = None
        form = LoginForm()

    c = {}
    c.update(csrf(request))
    return render(request, 'login.jinja',
        {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

