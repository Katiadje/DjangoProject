from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('banner/', views.banner, name='banner'),
    path('countries/', views.countries, name='countries'),
    path('cities/', views.cities, name='cities'),
    path('films/', views.films, name='films'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)