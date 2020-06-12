from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.models import User

from .forms import CreateStartupForm
from .models import Account, Startup, Request

# from ..test import Test

# Create your views here.

def create_startup(request):
    if request.method == 'POST':
        filled_form = CreateStartupForm(request.POST)
        if filled_form.is_valid():
            note = "Your startup has been created!"
            new_startup = filled_form.save()
            return render(request, 'create_startup.html', {'note': note})
    else:
        createStartupForm = CreateStartupForm()
        return render(request, 'create_startup.html', {'createStartupForm': createStartupForm})
