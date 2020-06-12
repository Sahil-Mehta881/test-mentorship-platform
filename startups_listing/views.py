from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.models import User

from .forms import SearchStartupForm, CreateStartupForm
from .models import Account, Startup, Request, Proxy


class Query:
    query = None

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

def startups_listing(request):
    if request.method == 'POST':
        filled_form = SearchStartupForm(request.POST)
        if filled_form.is_valid():
            Query.query = filled_form.cleaned_data['name']
            filteredStartups = [startup for startup in Startup.objects.all() if startup.name == Query.query]
            searchStartupForm = SearchStartupForm()
            return render(request, 'startups_listing.html', {'object_list': filteredStartups, 'searchStartupForm': searchStartupForm})
    else:
        object_list = Startup.objects.all()
        searchStartupForm = SearchStartupForm()
        return render(request, 'startups_listing.html', {'object_list': object_list, 'searchStartupForm': searchStartupForm})
