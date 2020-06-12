from django import forms
from .models import Startup

class CreateStartupForm(forms.ModelForm):

    class Meta:
        model = Startup
        fields = ['name', 'description']
