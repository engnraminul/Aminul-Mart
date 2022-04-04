from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from Payment.models import BillingAddress
from Payment.forms import BillingAddressForm, PaymentMethodForm
from Order.models import Cart, CartToOrder

from django.views.generic import TemplateView


class CheckoutView(TemplateView):
    def get(self, request,*args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form =BillingAddressForm(instance=saved_address)
        payment_method = PaymentMethodForm()

        order_qs = CartToOrder.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_totals = order_qs[0].get_totals_price()

        context = {
            'billingaddress': form,
            'order_item': order_item,
            'order_totals': order_totals,
            'payment_method': payment_method,
        }

        return render(request, 'shop/checkout.html', context)


    def post(self, request, *args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        billing_form = BillingAddressForm(instance=saved_address)
        payment_obj = CartToOrder.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)
        if request.method == 'POST' or request.method == 'post':
            Bill_address_form = BillingAddressForm(request.POST, instance=saved_address)
            pay_form = PaymentMethodForm(request.POST, instance=payment_obj)
            if Bill_address_form.is_valid() and pay_form.is_valid():
                Bill_address_form.save()
                pay_method = pay_form.save()


                if not saved_address.is_fully_filled():
                    return redirect('Payment:checkout')

                if pay_method.payment_method == 'Cash on Delivery':
                    order_qs = CartToOrder.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.orderId = order.id
                    order.paymentId = pay_method.payment_method
                    order.save()
                    cart_items = Cart.objects.filter(user=request.user, purchased=False)
                    for item in cart_items:
                        item.purchased = True
                        item.save()
                    return redirect('Shop:home')
