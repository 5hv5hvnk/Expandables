from django.urls import path, include
from . import views

urlpatterns = [
    path('map', views.map, name = 'map'),
]