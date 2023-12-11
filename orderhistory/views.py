from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import FinishedOrder

# @login_required
def order_history(request):
    orders = FinishedOrder.objects.all  # Change the filtering based on your model structure
    return render(request, 'order_history.html', {'orders': orders})
