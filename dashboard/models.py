from django.db import models

# store user info
# each class is an SQL table

class Account(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    linkedInUrl = models.CharField(max_length=50)

    OCC_CHOICES = [('S', 'Student'), ('F', 'Faculty'), ('O', 'Other')]
    occupation = models.CharField(choices=OCC_CHOICES, max_length=1)


class Startup(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)


class Request(models.Model):
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=600)

    # placeholder array, must load all mentors available
    MENTOR_CHOICES = [('mentor-one', 'mentor-one'), ('mentor-two', 'mentor-two')]
    mentor = models.CharField(choices=MENTOR_CHOICES, max_length=20, default="")
