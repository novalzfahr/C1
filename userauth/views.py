# ---- Django Imports ----
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core import serializers
from datetime import datetime

# ---- App Imports ----
from .forms import RegistrationForm, LoginForm
from .models import UserDataModel

# Create your views here.
# ---- UserAuth Related Methods ----
@csrf_exempt
def userauth_home(request):        
    form = LoginForm()
    users = UserDataModel.objects.all()
    logged_in = request.user
    try:
        logged_in = UserDataModel.objects.get(id=logged_in.id).name
    except:
        pass
    context = {
        'form':form,
        'user_list':serializers.serialize("json", users),
        'logged_in':logged_in,
    }
    if request.method == 'POST':
        button_press = request.POST.get('register_or_login')
        if button_press == 'to_register':
            return redirect('userauth:register')
        elif button_press == 'to_login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = UserDataModel.objects.get(username=username, password=password)
                login(request, user)
                return redirect('userauth:userauth_home')
            except:
                messages.info(request, 'Username atau Password salah!')
        elif button_press == 'to_logout':
            return logout(request)
    
    return render(request, 'userauth_home.html', context)

@csrf_exempt
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Akun telah berhasil dibuat!')
                print('success')
                return redirect('userauth:userauth_home')
            except ValueError:
                messages.info("Name cannot be empty")
    
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def logout(requested):
    '''
    
    How to use in other methods:
    
    from userauth.views import logout
    def function(request):
      ...
      return logout(request)
    
    '''
    requested.session.flush()
    requested.session.clear_expired()
    return redirect('userauth:userauth_home')


# ---- User Account Details Related Methods ----
def show_profile(request):
    current_user = UserDataModel.objects.get(id=request.user.id)