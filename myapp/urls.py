from django.conf.urls import url
from django.contrib.auth import logout
from django.urls import path
from .views import home, delete, loginPAGE, logoutPAGE, pages, register
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('',register,name='register'),
    path('login/',loginPAGE,name='login'),
    path('logout/',logoutPAGE,name='logout'),


    path('home/',home,name='home'),
    path('page/<int:pk>/',pages,name='page'),
    path('delete/<int:pk>',delete,name='delete'),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_done.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/complete.html'),name="password_reset_complete"),
]
