from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('landing/', views.landing, name='landing'),
    path('index/', views.index, name='index'),
]
