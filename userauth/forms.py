# ---- Django Imports ----
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# ---- App Imports ----
from .models import UserDataModel

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserDataModel
        fields = ['username', 'password', 'role', 'name', 'email', 'phone_number']
        widgets = {
            'password':forms.PasswordInput()
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = UserDataModel
        fields = ['username', 'password']
        widgets = {
            'password':forms.PasswordInput()
        }
    # username = forms.CharField(label='Username')
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)
