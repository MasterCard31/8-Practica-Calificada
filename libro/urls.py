from django.urls import path

from . import views

urlpatterns = [
    path('', views.libro, name='libro'),
]