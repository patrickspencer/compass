from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# ...
def home(request):
    return render(request, 'base.html', {
        'welcome_message': 'Hello world!',
    })
