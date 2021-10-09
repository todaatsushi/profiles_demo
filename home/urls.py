from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-this-project/", views.about_project, name="about_project"),
]
