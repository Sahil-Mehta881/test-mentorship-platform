from django import forms
from .models import Mentor

class SearchMentorForm(forms.Form):
    name = forms.CharField(label='Mentor Name', max_length=20)
