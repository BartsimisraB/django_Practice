"""A0403 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from first import views
#
# urlpatterns = [
#     path('', views.index, name='index'),  # views 파일의 index 메소드에 연결
#     path('admin/', admin.site.urls),
#
# ]
from django.contrib import admin
from django.urls import path, include
from first import views

urlpatterns = [
    # views 파일의 index 메소드에 연결

    # path('', include('first.urls')), # first 앱의 urls와 연결
    # path('', include('two.urls')),    # two 앱의 urls와 연결
    path('three/', include('three.urls')),  # three 앱의 urls와 연결
    path('admin/', admin.site.urls),

]
