from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from order.models import *
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='userauth:userauth_home')
def read_menu(request):
    menu = Menu.objects.all()
    context = {
        'menu': menu,
    }
    return JsonResponse(context)

@login_required(login_url='userauth:userauth_home')
def add_menu_to_cart(request, menu_id):
    menu = Menu.objects.get(ID_menu=menu_id)
    user = request.user
    item, created = Item.objects.get_or_create(user=user, nama_item=menu.nama)
    if not created:
        item.kuantitas += 1
        item.save()
    return HttpResponseRedirect('/order_home/')

@login_required(login_url='userauth:userauth_home')
def delete_item_from_cart(request, item_id):
    try:
        item = Item.objects.filter(user=request.user).get(id=item_id)
        item.delete()
        return HttpResponseRedirect('/order_home/')
    except ObjectDoesNotExist:
        return render(request, 'error_page.html', {'message': 'Item does not exist'})
    except Item.MultipleObjectsReturned:
        return render(request, 'error_page.html', {'message': 'Multiple items found'})

@login_required(login_url='userauth:userauth_home')
def change_item_quantity(request, item_id, quantity_change):
    item = Item.objects.filter(user=request.user).get(id=item_id)
    item.kuantitas += quantity_change
    if item.kuantitas < 0:
        return render(request, 'error_page.html', {'message': 'Item quantity cannot be less than zero'})
    elif item.kuantitas == 0:
        item.delete()
    else:
        item.save()
    return HttpResponseRedirect('/order_home/')