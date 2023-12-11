# ---- Django Imports ----
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# ---- App Imports ----
from .models import UserDataModel

class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = UserDataModel
        fields = ['username', 'role', 'name', 'email', 'phone_number', 'password']
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

class EditEmailForm(forms.ModelForm):
    class Meta:
        model = UserDataModel
        fields = ['email']

class EditPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = UserDataModel
        fields = ['phone_number']

class EditPasswordForm(forms.ModelForm):
    password_confirm = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = UserDataModel
        fields = ['password']
        widgets = {
            'password':forms.PasswordInput()
        }