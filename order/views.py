from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from order.models import *

# Create your views here.
@login_required(login_url='userauth:userauth_home')
def read_menu(request):
    user = request.user
    menu = Menu.objects.all()
    context = {
        'menu': menu,
        'user': user,
    }
    return render(request, 'order_home.html', context)

def display_cart(request):
    user = request.user
    items = Item.objects.filter(user=user)
    total = total_price(request)
    context = {
        'items': items,
        'user': user,
        'total': total,
    }
    return render(request, 'cart.html', context)

def add_menu_to_cart(request, menu_id):
    if request.method == 'POST':
        menu = Menu.objects.get(ID_menu=menu_id)
        user = request.user
        
        # Cek jika item sudah ada di cart untuk user saat ini
        try:
            item = Item.objects.get(user=user, nama_item=menu.nama)
            if item.kuantitas > 0:
                messages.warning(request, f"{menu.nama} already in cart.")
                return HttpResponseRedirect('/order/')
        except Item.DoesNotExist:
            pass
        
        # Mencari ID_item maksimum dan menambahkannya untuk item baru
        max_id_item = Item.objects.aggregate(models.Max('ID_item'))['ID_item__max']
        new_id_item =  str(int(max_id_item) + 1) if max_id_item else '1'

        # Menambahkan item baru ke cart
        item, created = Item.objects.get_or_create(
            user=user, nama_item=menu.nama, harga=menu.harga,
            defaults={'ID_item': new_id_item}
        )
        if not created:
            item.kuantitas += 1
            item.save()
        messages.success(request, f"{menu.nama} added to cart successfully.")

    return HttpResponseRedirect('/order/')

@login_required(login_url='userauth:userauth_home')
def delete_item_from_cart(request, item_id):
    item = get_object_or_404(Item, ID_item=item_id, user=request.user)
    item.delete()
    messages.info(request, f"{item.nama_item} deleted successfully.")
    
    return HttpResponseRedirect('/order/cart')

@login_required(login_url='userauth:userauth_home')
def change_item_quantity(request, item_id, quantity_change):
    item = get_object_or_404(Item, ID_item=item_id, user=request.user)

    # Change the item quantity based on the provided value
    if quantity_change == '1':
        item.kuantitas += 1
    elif quantity_change == '-1' and item.kuantitas > 0:
        item.kuantitas -= 1
        if item.kuantitas == 0:
            item.kuantitas = 1
            messages.warning(request, f"{item.nama_item} cannot zero.")
    item.save()
    
    return HttpResponseRedirect('/order/cart')

    # return redirect('order:display_cart')

def total_price(request):
    user = request.user
    items = Item.objects.filter(user=user)
    total = 0
    for item in items:
        total += item.harga*item.kuantitas
    return total