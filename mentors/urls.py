from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor_listing, name="mentor_listing"),
]
