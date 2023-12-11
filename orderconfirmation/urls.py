from django.urls import path
from .views import order_list, accept_order, reject_order

urlpatterns = [
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/accept/', accept_order, name='accept_order'),
    path('orders/<int:order_id>/reject/', reject_order, name='reject_order'),
]
