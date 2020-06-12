from django.urls import path
from . import views

urlpatterns = [
    path('listing', views.startups_listing, name="startups_listing"),
    path('create', views.create_startup, name="create_startup"),
]
