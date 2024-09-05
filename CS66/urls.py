from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexpage, name='index'),
    path("login/", views.loginpage, name='login'),
    path("register/", views.registerpage, name='register'),
    path("about/", views.aboutpage, name='about'),
]
