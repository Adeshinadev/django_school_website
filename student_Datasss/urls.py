"""secschoolportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView
urlpatterns = [


    path('search/', views.search, name='search'),
    path('search_r/', views.search_r, name='search_r'),
    path('test/', views.test, name='test'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('Idcard/', views.Idcard, name='Idcard'),
    path('Enter_result',views.Enter_result, name='Enter_result'),
    path('check_result', views.check_result, name='check_result'),

]
