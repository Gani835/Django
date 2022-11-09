from django.contrib import admin
from django.urls import path
from secondapp import views
urlpatterns = [
    path('signup',views.usersignup,name='createuser'),
    path('login',views.userlogin,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('home',views.homepage,name='home'),
]