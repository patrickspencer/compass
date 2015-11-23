from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render
from apps.staff.forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib import messages


def admin_view(request):
    return render(request, 'staff/base.jinja', {})

def users_new_view(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                # messages = "User with that email already exists"
                pass
            else:
                User.objects.create_user(
                        username = form.cleaned_data['username'],
                        email = email,
                        password = form.cleaned_data['password'],
                        last_name = form.cleaned_data['last_name'],
                        first_name = form.cleaned_data['first_name']
                        )
                # messages = "User created"
    else:
        form = NewUserForm()
    messages.add_message(request, messages.INFO, 'This is a message!.')
    return render(request, 'users/new.html', {
        'form': form,
        # 'messages': messages
    })

