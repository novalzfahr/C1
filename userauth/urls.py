# ---- Django Imports ----
from django.urls import path

# ---- App Imports ----
from .views import register, userauth_home

app_name = 'userauth'

urlpatterns = [
    path('', userauth_home, name='userauth_home'),
    path('register/', register, name='register'),
]