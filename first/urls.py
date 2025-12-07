from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('https://firstapptesting-hteuf3czeed2bzdu.centralus-01.azurewebsites.net/', index, name = 'index'),
    path('https://firstapptesting-hteuf3czeed2bzdu.centralus-01.azurewebsites.net/webhook/', webhook, name = 'webhook'),
]
