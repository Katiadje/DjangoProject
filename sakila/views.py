from django.shortcuts import render, redirect,get_object_or_404
from .models import Country, City, User, Film  # Film ajouté
import base64

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

# def cities(request):
#     cities = City.objects.all().select_related('country')
#     return render(request, 'cities.html', {'cities': cities})

def banner(request):
    return render(request, 'banner.html')

def films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})



def city_detail(request, city_id):
    # city = get_object_or_404(City, pk=city_id)
    city = get_object_or_404(City, pk=city_id)
    if city.picture:
        city.picture_base64 = base64.b64encode(city.picture).decode('utf-8')
    else:
        city.picture_base64 = None
    return render(request, 'city_detail.html', {'city': city})



def cities(request):
    cities = City.objects.all()

    for city in cities:
        if city.picture:
            city.picture_base64 = base64.b64encode(city.picture).decode('utf-8')
        else:
            city.picture_base64 = None

    return render(request, 'cities.html', {'cities': cities})

def cities(request):
    cities = City.objects.all()

    for city in cities:
        city.has_picture = bool(city.picture)  # True si city.picture existe, sinon False

    return render(request, 'cities.html', {'cities': cities})