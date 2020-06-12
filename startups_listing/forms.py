from django import forms
from .models import Startup

class SearchStartupForm(forms.Form):
    name = forms.CharField(label='Startup Name', max_length=20)

class CreateStartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = ['name', 'description']
