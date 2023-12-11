from django.urls import path
from .views import order_history

urlpatterns = [
    path('orderhistory/', order_history, name='order_history'),
]