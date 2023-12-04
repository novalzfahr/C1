# ---- Django Imports ----
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from datetime import datetime

# ---- App Imports ----
from .forms import RegistrationForm, LoginForm, EditEmailForm, EditPhoneNumberForm, EditPasswordForm
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
                next_page = request.POST.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('userauth:profile_page')
            except:
                messages.info(request, 'Username atau Password salah!')
        # elif button_press == 'to_logout':
        #     return logout(request)
    
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
                messages.info(request, "Pastikan kembali data isian benar")
    
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

    # # Reminder :coba setting session expire # settings.py

    # # Set the session expiration duration in seconds (e.g., 30 minutes)
    # SESSION_EXPIRE_SECONDS = 1800  # 30 minutes



# ---- User Account Details Related Methods ----
@login_required(login_url='/userauth/')
def show_profile(request):
    current_user = UserDataModel.objects.get(id=request.user.id)
    context = {
        'user':current_user
    }

    if request.method == 'POST':
        button_press = request.POST.get('page_switch')
        if button_press == 'to_logout':
            return logout(request)
        elif button_press == 'to_edit':
            return redirect('userauth:edit_profile_page')
        
    return render(request, 'user_profile.html', context)

@login_required(login_url='/userauth/')
def edit_profile_page(request):
    
    if request.method == 'POST':
        button_press = request.POST.get('page_switch')
        if button_press == 'to_cancel':
            return redirect('userauth:profile_page')
        elif button_press == 'edit_email':
            return redirect('userauth:edit_email_page')
        elif button_press == 'edit_phone_number':
            return redirect('userauth:edit_phone_number_page')
        elif button_press == 'edit_password':
            return redirect('userauth:edit_password_page')
        
    return render(request, 'edit_profile.html')

@login_required(login_url='/userauth/')
def edit_email(request):
    form = EditEmailForm()
    if request.method == 'POST':
        if request.POST.get('submit') == 'to_cancel':
                return redirect('userauth:profile_page')

        current_user = request.user
        new_email = request.POST.get('email')
        try:
            print(current_user.email, new_email)
            if current_user.email == new_email:
                messages.info(request, "Email baru sama dengan email yang sedang digunakan")
            else:
                UserDataModel.objects.get(email=new_email)
                messages.info(request, "Email sudah digunakan")
        except:
            form = EditEmailForm(request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                return redirect('userauth:profile_page')
    context = {
        'form':form
    }
    return render(request, 'edit_email_page.html', context)

@login_required(login_url='/userauth/')
def edit_phone_number(request):
    pass

@login_required(login_url='/userauth/')
def edit_password(request):
    pass