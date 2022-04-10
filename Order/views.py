from django.shortcuts import render, get_object_or_404, redirect
from Shop.models import Product
from Order.models import Cart, CartToOrder

from coupon.forms import CouponForm
from coupon.models import Coupon
from django.utils import timezone
# Create your views here.

def add_to_cart(request, pk):
    if request.user.is_authenticated:
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
    else:
        return redirect('Login:user_login')


def cart_view(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, purchased=False)
        orders = CartToOrder.objects.filter(user=request.user, ordered=False)
        code=""
        total_price_with_discount=0
        if carts.exists() and orders.exists():
            order = orders[0]
            coupon_form = CouponForm(request.POST)
            if coupon_form.is_valid():

                current_time = timezone.now()
                code = coupon_form.cleaned_data.get('code')
                coupon_object = Coupon.objects.get(code=code, active_status=True)
                if coupon_object.valid_to >= current_time:
                    get_discount = (coupon_object.discount / 100) * order.get_totals_price()
                    total_price_with_discount = order.get_totals_price() - get_discount
                    request.session['discount_total'] = total_price_with_discount
                    request.session['coupon_code'] = code
                    return redirect('Order:cart')
                else:
                    coupon_object.active_status = False
                    coupon_object.save()

            total_price_with_discount = request.session.get('discount_total')
            coupon_code = request.session.get('coupon_code')
            context = {
                'carts': carts,
                'order': order,
                'coupon_form': coupon_form,
                'coupon_code': coupon_code,
                'total_price_with_discount': total_price_with_discount,
            }
            return render(request, 'Shop/cart.html', context)
    else:
        return redirect('Login:user_login')




def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    orders = CartToOrder.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('Order:cart')
        else:
            return redirect('Order:cart')
    else:
        return redirect('Order:cart')


def increase_quantity(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = CartToOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return redirect('Order:cart')
            else:
                return redirect('Store:home')
        else:
            return redirect('Shop:home')
    else:
        return redirect('Shop:home')

def decrease_quantity(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = CartToOrder.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('Order:cart')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('Shop:home')
        else:
            return redirect('Shop:home')
    else:
        return redirect('Shop:home')
