from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='reg'),
    path('profile', views.profile, name='profile')
]