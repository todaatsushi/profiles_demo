from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_project, name="about_project"),
    path("find_me/", views.find_me, name="find_me"),
]
