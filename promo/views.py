from django.shortcuts import render, redirect, get_object_or_404
from order.models import Promo
from .forms import PromotionForm

def create_promo(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_promo')
    else:
        form = PromotionForm()
    return render(request, 'create_promo.html', {'form': form})

# @login_required(login_url='/userauth/')
def ubah_promo(request, id):
    item = get_object_or_404(Promo, ID_promo=id)
    if request.method == 'POST':
        form = PromotionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_promo')
    else:
        form = PromotionForm(instance=item)
    return render(request, 'create_promo.html', {'form': form})

# @login_required(login_url='/userauth/')
def hapus_promo(request, id):
    item = get_object_or_404(Promo, ID_promo=id)
    item.delete()
    return redirect('display_promo')


def display_promo(request):
    promo = Promo.objects.all()
    return render(request, 'promo_list.html', {'promo': promo}) 
