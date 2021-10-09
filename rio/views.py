from django.http import HttpResponse


def home(request):
    html = "<h1>Hello, World!</h1><a href='/about-this-project/'>About</a>"
    return HttpResponse(html)


def about_project(request):
    html = "<h1>This is a project made to learn django!</h1><a href='/'>Back home</a>"
    return HttpResponse(html)
