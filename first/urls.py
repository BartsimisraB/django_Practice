from django.urls import path
from . import views

# path(url 경로, 파일명.메소드명, nema=메서드 이름)
urlpatterns = [
    # path('', views.index, name='index'),
    # path('number/', views.number, name='number'),
    # path('result/', views.result, name='result'),
    path('list/', views.list, name='list'),
    path('fo/', views.fo, name='fo'),
    path('check/', views.check, name='check'),
]
