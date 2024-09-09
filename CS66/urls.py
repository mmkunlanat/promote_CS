from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexpage, name='index'),
    path("login/", views.loginpage, name='login'),
    path("register/", views.registerpage, name='register'),
    path("about/", views.aboutpage, name='about'),
    path("about1/", views.about1page, name='about1'),
    path("about2/", views.about2page, name='about2'),
    path("about3/", views.about3page, name='about3'),
]
