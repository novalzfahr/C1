from django.urls import path
from .views import create_promo, display_promo, hapus_promo, ubah_promo

urlpatterns = [
    path('create_promo/', create_promo, name='create_promo'),
    path('hapus_promo/<str:id>/', hapus_promo, name='hapus_promo'),
    path('ubah_promo/<str:id>/', ubah_promo, name='ubah_promo'),
    path('promo/', display_promo, name='display_promo'),
]
