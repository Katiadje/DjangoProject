from django.shortcuts import render, get_object_or_404
from .models import Country, City, Film

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})

def cities(request):
    show = request.GET.get('show', 'all')  # Récupère paramètre show ou 'all' par défaut

    if show == 'capitals':
        cities = City.objects.filter(capital=True).select_related('country')
    else:
        cities = City.objects.all().select_related('country')

    context = {
        'cities': cities,
        'show': show,
    }
    return render(request, 'cities.html', context)

def banner(request):
    return render(request, 'banner.html')

def films(request):
    films = Film.objects.all()
    return render(request, 'films.html', {'films': films})

def city_detail(request, city_id):
    city = get_object_or_404(City.objects.select_related('country'), city_id=city_id)
    return render(request, 'city_detail.html', {'city': city})
