from django.contrib import admin
from django.conf.urls import *
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('forgot-password/',views.forgot_password,name="forgot-password"),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login, name='login'),
    path("student/",views.student, name='student'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
 

]

