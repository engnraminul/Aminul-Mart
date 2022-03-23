from django.shortcuts import render, get_object_or_404, redirect
from Shop.models import Product
from Order.models import Cart, CartToOrder
# Create your views here.

def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
    order_qs = CartToOrder.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            variant = request.POST.get('variant')
            color = request.POST.get('color')
            quantity = request.POST.get('quantity')
            if quantity:
                order_item[0].quantity += int(quantity)
            else:
                order_item[0].quantity += 1
            order_item[0].variant=variant
            order_item[0].color=color
            order_item[0].save()
            return redirect('Shop:home')
        else:
            order.orderitems.add(order_item[0])
            return redirect('Shop:home')
    else:
        variant = request.POST.get('variant')
        color = request.POST.get('color')
        order_item[0].variant=variant
        order_item[0].color=color

        order = CartToOrder(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect('Shop:home')

def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = CartToOrder.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        context = {
            'carts': carts,
            'order': order,
        }
        return render(request, 'Shop/cart.html', context)
