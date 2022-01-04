from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('change_password/<token>', views.change_password, name='change_password'),


]