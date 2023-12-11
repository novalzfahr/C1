from django.shortcuts import render, redirect
from order.models import Promo
from .forms import PromotionForm

def create_promo(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            try:
                # Processing promotion creation
                form.save()
                # Update menu price based on the promotion
                # update_menu_price(form.cleaned_data['menu'], form.cleaned_data['discount_amount'])
                return redirect('display_promo')
            except Exception as e:
                return render(request, 'promo_error.html', {'error_message': str(e)})
    else:
        form = PromotionForm()

    return render(request, 'create_promo.html', {'form': form})


def display_promo(request):
    promo = Promo.objects.all()
    return render(request, 'promo_list.html', {'promo': promo}) 
