from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('', read_menu, name='userauth_home'),
    path('add_to_cart/<str:menu_id>/', add_menu_to_cart, name='add_menu_to_cart'),
    path('cart/', display_cart, name='display_cart'),
    path('delete-item/<str:item_id>/', delete_item_from_cart, name='delete-item'),
    path('change-item-quantity/<str:item_id>/<str:quantity_change>/', change_item_quantity, name='change-item-quantity'),
]