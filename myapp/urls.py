from django.urls import path
from .views import home, delete
urlpatterns = [
    path('',home,name='home'),
    path('delete/<int:pk>',delete,name='delete')
]