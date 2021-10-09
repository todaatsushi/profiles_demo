from django.http import HttpResponse


def home(request):
    html = "<h1>Hello, World!</h1"
    return HttpResponse(html)
