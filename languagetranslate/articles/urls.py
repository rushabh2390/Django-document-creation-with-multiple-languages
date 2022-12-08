from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('french/', views.french_title, name='french'),
    path('spanish/', views.spanish_title, name='spanish'),
]
