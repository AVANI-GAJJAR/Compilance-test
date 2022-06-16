from django import views
from django.contrib import admin
from django.urls import path
from PPI import views
urlpatterns = [
    path('', views.index,name="login"),
    path('auth',views.auth,name="auth"),
    path('filetype',views.filetype,name="auth"),
    ]