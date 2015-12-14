from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from apps.core.forms.login import LoginForm
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View


@method_decorator(login_required, name='dispatch')
class LoginRequiredView(View):
    pass


class Login(View):
    def post(self, request):
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
        return render(request, 'login.jinja', {'form': form})

    def get(self, request):
        user = None
        form = LoginForm()
        return render(request, 'login.jinja', {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login')

