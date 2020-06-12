from django.db import models

# Create your models here.

class Mentor(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    linkedInUrl = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=500)
