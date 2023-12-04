from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MenuItem
from .forms import MenuItemForm

@login_required
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu_list.html', {'items': items})

@login_required
def menu_create(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'menu_form.html', {'form': form})

@login_required
def menu_update(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu_form.html', {'form': form})

@login_required
def menu_delete(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu_confirm_delete.html', {'item': item})