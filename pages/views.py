from django.shortcuts import render
from cars.models import Car  # Keep this if you want cars on the home page

def home(request):
    cars = Car.objects.all()
    return render(request, 'pages/home.html', {'cars': cars})

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
