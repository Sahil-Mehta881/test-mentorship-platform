from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.models import User

from .forms import RequestForm
from .models import Account, Startup, Request

"""
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
"""

def dashboard(request):
    if request.method == 'POST':
        filled_form = RequestForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note = "Your feedback request is in review"
            return render(request, 'dashboard.html', {'note': note})
    else:
        requestForm = RequestForm()
        return render(request, 'dashboard.html', {'requestform': requestForm})

"""
def profile(request):
    return render(request, 'profile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def startups(request):
    return render(request, 'startups.html')

def mentors(request):
    return render(request, 'mentors.html')

def apply_mentor(request):
    return render(request, 'apply-mentor.html')

def create_startup(request):
    return render(request, 'create-startup.html')
"""
