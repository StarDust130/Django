from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Eternity Home Page! 😆")


def about(request):
    return HttpResponse("Hello Eternity About Page! ☺️")


def contact(request):
    return HttpResponse("Hello Eternity Contact Page! 🙂")
