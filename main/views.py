from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def contact(request):
    return render(request, 'main/contact.html')


def login(request):
    return render(request, 'main/login-page.html')


def profile(request):
    return render(request, 'main/profile-page.html')


def landing(request):
    return render(request, 'main/landing-page.html')


def index(request):
    return render(request, 'main/index.html')
