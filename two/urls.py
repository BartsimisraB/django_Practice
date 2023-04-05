from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('fo/', views.fo, name='fo'),
    path('check/', views.check, name='check'),
]
