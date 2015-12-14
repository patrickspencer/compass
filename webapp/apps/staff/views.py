from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse_lazy
from apps.staff.forms import UserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from apps.core.views import LoginRequiredView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


class Index(LoginRequiredView, ListView):
    model = User
    template_name = 'staff/users/users_index.jinja'

class Create(LoginRequiredView, CreateView):
    model = User
    fields = ['username','password', 'email', 'first_name', 'last_name']
    template_name = 'staff/users/users_new.jinja'
    success_url = reverse_lazy('staff:users_home')

class Delete(LoginRequiredView, DeleteView):
    model = User
    template_name = 'staff/users/users_confirm_delete.jinja'
    success_url = reverse_lazy('staff:users_home')

class Update(LoginRequiredView, UpdateView):
    model = User
    fields = ['username','email', 'first_name', 'last_name']
    template_name = 'staff/users/users_update.jinja'
    success_url = reverse_lazy('staff:users_home')





