from django.shortcuts import render, redirect
from .models import Country, City, User, Film  # Film ajouté

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def cities(request):
    cities = City.objects.all().select_related('country')
    return render(request, 'cities.html', {'cities': cities})

def banner(request):
    return render(request, 'banner.html')

def films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})
