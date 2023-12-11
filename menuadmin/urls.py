from django.urls import path
from .views import menu_list, menu_create, menu_update, menu_delete

urlpatterns = [
    path('menu/', menu_list, name='menu_list'),
    path('menu/create/', menu_create, name='menu_create'),
    path('menu/update/<int:pk>/', menu_update, name='menu_update'),
    path('menu/delete/<int:pk>/', menu_delete, name='menu_delete'),
]