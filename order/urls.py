from django.urls import path
from order.views import *

app_name = 'order'

urlpatterns = [
    path('', read_menu, name='userauth_home'),
    # path('read_menu', read_menu, name='read_menu'),

]