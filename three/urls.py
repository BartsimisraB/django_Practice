from django.urls import path
from . import views

urlpatterns = [
    path('li/', views.li, name='li'),
    path('basic/', views.basic, name='basic')
]