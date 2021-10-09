from django.shortcuts import render
from django.utils.timezone import now
from geocoder import ip


def home(request):
    name = "Amane"
    return render(request, "home/home.html", {"name": name})


def about_project(request):
    today_date = now()
    return render(request, "home/about_project.html", {"today_date": today_date})


def find_me(request):
    g = ip("me")
    lat_long = g.latlng
    address = [g.city, g.country]
    full_info = g.json
    return render(
        request,
        "home/find_me.html",
        {
            "lat_long": lat_long,
            "address": address,
            "full_info": full_info,
        },
    )
