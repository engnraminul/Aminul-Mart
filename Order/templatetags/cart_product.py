from django import template
from Order.models import Cart, CartToOrder

register = template.Library()

@register.filter
def cart_view(user):
    cart = Cart.objects.filter(user=user, purchased=False)
    if cart.exists():
        return cart
    else:
        return cart

@register.filter
def cart_total(user):
    order = CartToOrder.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].get_totals_price()
    else:
        return 0


@register.filter
def cart_count(user):
    order = CartToOrder.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0
