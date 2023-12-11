from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from order.models import Menu
from .forms import MenuItemForm

# @login_required(login_url='/userauth/')
def menu_list(request):
    menu = Menu.objects.all()
    return render(request, 'menu_list.html', {'menu': menu})

# @login_required(login_url='/userauth/')
def menu_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu_form.html', {'form': form})

# @login_required(login_url='/userauth/')
def menu_update(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu_form.html', {'form': form})

# @login_required(login_url='/userauth/')
def menu_delete(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'confirm_delete.html', {'item': item})