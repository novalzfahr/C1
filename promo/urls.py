from django.urls import path
from .views import create_promo, display_promo

urlpatterns = [
    path('create_promo/', create_promo, name='create_promo'),
    path('display_promo/', display_promo, name='display_promo'),
]
