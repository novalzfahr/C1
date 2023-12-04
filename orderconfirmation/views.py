from django.shortcuts import render, get_object_or_404, redirect
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def accept_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    try:
        # Processing the order
        order.status_order = 'processed'
        order.save()
        return redirect('order_list')
    except Exception as e:
        return render(request, 'error_notification.html', {'error_message': str(e)})

def reject_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    try:
        # Rejecting the order
        order.status_order = 'canceled'
        order.save()
        return redirect('order_list')
    except Exception as e:
        return render(request, 'error_notification.html', {'error_message': str(e)})
