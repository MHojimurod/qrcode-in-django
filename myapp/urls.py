

from django.conf.urls import url
from django.contrib.auth import logout
from django.urls import path
from .views import home, delete, loginPAGE, logoutPAGE, register
from django.contrib.auth.models import User
urlpatterns = [
    path('home/',home,name='home'),
    path('delete/<int:pk>',delete,name='delete'),
    path('',register,name='register'),
    path('login/',loginPAGE,name='login'),
    path('logout/',logoutPAGE,name='logout'),
]
