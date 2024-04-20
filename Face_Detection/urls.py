from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name = "home"),
    path('register/',register,name = 'register'),
    path('login/',login,name = 'login'),
    path('about/',about,name = 'about'),
    path('team/',team,name = 'team'),
    path('greeting/<face_id>/',Greeting,name='greeting'),
    path('staff/',searchAttendence,name='staff'),
]
