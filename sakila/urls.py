from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.banner, name='banner'),
    path('countries/', views.countries, name='countries'),
    path('cities/', views.cities, name='cities'),
    path('films/', views.films, name='films'),
]
