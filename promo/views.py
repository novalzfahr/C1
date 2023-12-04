from django.shortcuts import render, redirect
from .models import Promotion
from .forms import PromotionForm

def create_promo(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            try:
                # Processing promotion creation
                form.save()
                # Update menu price based on the promotion
                update_menu_price(form.cleaned_data['menu'], form.cleaned_data['discount_amount'])
                return render(request, 'promo_success.html')
            except Exception as e:
                return render(request, 'promo_error.html', {'error_message': str(e)})
    else:
        form = PromotionForm()

    return render(request, 'create_promo.html', {'form': form})

def update_menu_price(menu, discount_amount):
    menu.price -= discount_amount
    menu.save()
