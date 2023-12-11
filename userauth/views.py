# ---- Django Imports ----
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers

# ---- Py Package Imports ----
# from twilio.rest import Client
from datetime import datetime
import smtplib
import random
import string

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
            if request.POST.get('password_confirm') == request.POST.get('password'):
                try:
                    form.save()
                    messages.success(request, 'Akun telah berhasil dibuat!')
                    print('success')
                    return redirect('userauth:userauth_home')
                except ValueError:
                    messages.info(request, "Pastikan kembali data isian benar")
            else:
                messages.info(request, 'Password tidak sama!')
    
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def logout(request):
    '''
    
    How to use in other methods:
    
    from userauth.views import logout
    def function(request):
      ...
      return logout(request)
    
    '''

    request.session.flush()
    request.session.clear_expired()
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
            # TODO : make a way to connect this to otp_page
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
    form = EditPhoneNumberForm()
    if request.method == 'POST':
        if request.POST.get('submit') == 'to_cancel':
                return redirect('userauth:profile_page')

        current_user = request.user
        new_phone_number = request.POST.get('phone_number')
        try:
            print(current_user.phone_number, new_phone_number)
            if current_user.phone_number == new_phone_number:
                messages.info(request, "Nomor baru sama dengan nomor yang sedang digunakan")
            else:
                UserDataModel.objects.get(phone_number=new_phone_number)
                messages.info(request, "Nomor telepon sudah digunakan")
        except:
            # TODO : make a way to connect this to otp_page
            form = EditPhoneNumberForm(request.POST, instance=current_user)
            if form.is_valid():
                form.save()
                return redirect('userauth:profile_page')
    context = {
        'form':form
    }
    return render(request, 'edit_phone_number_page.html', context)

@login_required(login_url='/userauth/')
def edit_password(request):
    form = EditPasswordForm()
    if request.method == 'POST':
        if request.POST.get('submit') == 'to_cancel':
                return redirect('userauth:profile_page')

        current_user = request.user
        new_password = request.POST.get('password')
        print(current_user.password, new_password)
        if current_user.password == new_password:
            messages.info(request, "Password baru sama dengan password yang sedang digunakan")
        else:
            # TODO : make a way to connect this to otp_page
            form = EditPasswordForm(request.POST, instance=current_user)
            if form.is_valid():
                if request.POST.get('password_confirm') == request.POST.get('password'):
                    form.save()
                    new_login = UserDataModel.objects.get(username=current_user.username, password=new_password)
                    login(request, new_login)
                    return redirect('userauth:profile_page')
                else:
                    messages.info(request, 'Password tidak sama!')
    context = {
        'form':form
    }
    return render(request, 'edit_password_page.html', context)



'''
---- OTP Related Methods ----
For now, will not be used because it requires us to pay $0.5 a month which isn't much but I'd rather wait till we actually need to present the code (unfortunately, might cause a disaster).
'''
# def OTP_manager(media='', address=''):
#     char_choices = string.ascii_uppercase + string.digits
#     otp = ''.join(random.choices(char_choices, k=6))

#     if media == 'email':
#         sender_email = 'aplikasilaper@example.com'
#         sender_password = 'tugaskelompokrplc1'

#         subject = 'Your One-Time Password (OTP)'
#         body = f'Your OTP is: {otp}'

#         message = f'Subject: {subject}\n\n{body}'

#         try:
#             with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server and port
#                 server.starttls()
#                 server.login(sender_email, sender_password)
#                 server.sendmail(sender_email, address, message)
#             print('Email sent successfully!')
#         except Exception as e:
#             print(f'Error: {e}')

#     elif media == 'sms':
#         account_sid = 'your_account_sid'  # Replace with your Twilio account SID
#         auth_token = 'your_auth_token'  # Replace with your Twilio auth token
#         twilio_phone_number = 'your_twilio_phone_number'  # Replace with your Twilio phone number

#         client = Client(account_sid, auth_token)
#         try:
#             message = client.messages.create(
#                 body=f'Your OTP is: {otp}',
#                 from_=twilio_phone_number,
#                 to=address
#             )
#             print('SMS sent successfully!')
#             print(f'Message SID: {message.sid}')
#         except Exception as e:
#             print(f'Error: {e}')



# @login_required(login_url='/userauth/')
# def otp_page(request):
#     return render(request, 'otp_page.html')