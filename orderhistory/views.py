from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)  # Change the filtering based on your model structure
    return render(request, 'order_history.html', {'orders': orders})
