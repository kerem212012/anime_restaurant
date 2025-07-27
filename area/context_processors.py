from .models import Order

def cart_info(request):
    if not request.user.is_authenticated:
        return {'cart_count': 0, 'cart_total': 0}

    order = Order.objects.filter(user=request.user, is_draft=True).first()
    if not order:
        return {'cart_count': 0, 'cart_total': 0}

    items = order.orders.all()
    return {
        'cart_count': sum(item.quantity for item in items),
        'cart_total': sum(item.price * item.quantity for item in items),
    }
