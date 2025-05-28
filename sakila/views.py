# views.py
import base64
from django.shortcuts import render, get_object_or_404
from .models import Country, City

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def cities(request):
    show = request.GET.get('show', 'all')

    if show == 'capitals':
        cities = City.objects.filter(capital=True).select_related('country')
    else:
        cities = City.objects.all().select_related('country')

    # Encoder l'image binaire en base64 pour chaque ville
    for city in cities:
        if city.picture:
            city.picture_base64 = base64.b64encode(city.picture).decode('utf-8')
        else:
            city.picture_base64 = None

    context = {
        'cities': cities,
        'show': show,
    }
    return render(request, 'cities.html', context)

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    if city.picture:
        city.picture_base64 = base64.b64encode(city.picture).decode('utf-8')
    else:
        city.picture_base64 = None
    return render(request, 'city_detail.html', {'city': city})

def banner(request):
    return render(request, 'banner.html')
