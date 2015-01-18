from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render


def admin_view(request):
    return render(request, 'staff/base.html', {
        'user': request.user,
    })

