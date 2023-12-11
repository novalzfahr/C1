# ---- Django Imports ----
from django.urls import path

# ---- App Imports ----
from .views import register, logout, userauth_home, show_profile, edit_profile_page, edit_email, edit_phone_number, edit_password #, otp_page

app_name = 'userauth'

urlpatterns = [
    path('', userauth_home, name='userauth_home'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', show_profile, name='profile_page'),
    path('edit_profile/', edit_profile_page, name='edit_profile_page'),
    path('edit_profile/edit_email/', edit_email, name='edit_email_page'),
    path('edit_profile/edit_phone_number/', edit_phone_number, name='edit_phone_number_page'),
    path('edit_profile/edit_password/', edit_password, name='edit_password_page'),
    # path('edit_profile/otp_verification/', otp_page, name='otp_page'),
]