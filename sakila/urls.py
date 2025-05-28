from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.banner, name='banner'),
    path('countries/', views.countries, name='countries'),
    path('cities/', views.cities, name='cities'),

    # route détail ville
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
]
