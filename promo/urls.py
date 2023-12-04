from django.urls import path
from .views import create_promo

urlpatterns = [
    path('create_promo/', create_promo, name='create_promo'),
]
