from django import forms
from .models import Request

class RequestForm(forms.ModelForm):

    image = forms.ImageField()

    class Meta:
        model = Request
        fields = ['mentor', 'subject', 'message']
    """
    mentor = forms.ChoiceField(label="Mentor", choices = [("mentor-one", "mentor-one"), ("mentor-two", "mentor-two")])
    # choice array is a placeholder - mentors must be queried from database
    # for each choice, first entry is the visual and second is the value submitted by form

    subject = forms.CharField(label="Subject", max_length=50)
    message = forms.CharField(label="Message", max_length=500)
    """
