from django.shortcuts import render
from django.utils.timezone import now


def home(request):
    name = "Amane"
    return render(request, "home/home.html", {"name": name})


def about_project(request):
    today_date = now()
    return render(request, "home/about_project.html", {"today_date": today_date})
