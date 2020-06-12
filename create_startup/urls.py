from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_startup, name="create_startup"),
]
