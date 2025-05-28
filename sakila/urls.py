from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.countries, name='countries'),
    path('cities/', views.cities, name='cities'),
    path('banner/', views.banner, name='banner'),
    path('films/', views.films, name='films'),  # ajout pour films
]
