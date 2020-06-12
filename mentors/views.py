from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *

from .models import Mentor
from .forms import SearchMentorForm

# Create your views here.

class Query:
    query = None


def mentor_listing(request):
    if request.method == 'POST':
        filled_form = SearchMentorForm(request.POST)
        if filled_form.is_valid():
            Query.query = filled_form.cleaned_data['name']
            filteredMentors = [mentor for mentor in Mentor.objects.all() if mentor.name == Query.query]
            searchMentorForm = SearchMentorForm()
            return render(request, 'mentor_listing.html', {'object_list': filteredMentors, 'searchMentorForm': searchMentorForm})
    else:
        object_list = Mentor.objects.all()
        searchMentorForm = SearchMentorForm()
        return render(request, 'mentor_listing.html', {'object_list': object_list, 'searchMentorForm': searchMentorForm})
