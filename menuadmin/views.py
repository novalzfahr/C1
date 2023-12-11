from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Menu
from userauth.models import UserDataModel
from .forms import MenuItemForm

@login_required(login_url='/userauth/')
def menu_list(request):
    current_user = UserDataModel.objects.get(id=request.user.id)
    if current_user.role == 'admin':
        menu = Menu.objects.all()
        return render(request, 'menu_list.html', {'menu': menu})
    else:
        messages.info(request, "Kamu bukan admin, silahkan login kembali")
        return redirect ('/')

@login_required(login_url='/userauth/')
def menu_create(request):
    current_user = UserDataModel.objects.get(id=request.user.id)
    if current_user.role == 'admin':
        if request.method == 'POST':
            form = MenuItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('menu_list')
        else:
            form = MenuItemForm()
        return render(request, 'menu_form.html', {'form': form})
    else:
        messages.info(request, "Kamu bukan admin, silahkan login kembali")
        return redirect ('/')

@login_required(login_url='/userauth/')
def menu_update(request, pk):
    current_user = UserDataModel.objects.get(id=request.user.id)
    if current_user.role == 'admin':
        item = get_object_or_404(Menu, pk=pk)
        if request.method == 'POST':
            form = MenuItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('menu_list')
        else:
            form = MenuItemForm(instance=item)
        return render(request, 'menu_form.html', {'form': form})
    else:
        messages.info(request, "Kamu bukan admin, silahkan login kembali")
        return redirect ('/')

@login_required(login_url='/userauth/')
def menu_delete(request, pk):
    current_user = UserDataModel.objects.get(id=request.user.id)
    if current_user.role == 'admin':
        item = get_object_or_404(Menu, pk=pk)
        if request.method == 'POST':
            item.delete()
            return redirect('menu_list')
        return render(request, 'confirm_delete.html', {'item': item})
    else:
        messages.info(request, "Kamu bukan admin, silahkan login kembali")
        return redirect ('/')