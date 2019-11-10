from django.urls import path, include
from . import views

urlpatterns = [
    path('services', views.services, name = 'services'),
]