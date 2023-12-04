# ---- Django Imports ----
from django.urls import path

# ---- App Imports ----
from .views import register, userauth_home, show_profile

app_name = 'userauth'

urlpatterns = [
    path('', userauth_home, name='userauth_home'),
    path('register/', register, name='register'),
    path('profile/', show_profile, name='profile'),
]