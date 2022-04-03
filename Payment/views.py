from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from Payment.models import BillingAddress
from Payment.forms import BillingAddressForm
from Order.models import Cart, CartToOrder

from django.views.generic import TemplateView


class CheckoutView(TemplateView):
    def get(self, request,*args, **kwargs):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form =BillingAddressForm(instance=saved_address)

        order_qs = CartToOrder.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_totals = order_qs[0].get_totals_price()

        context = {
            'billingaddress': form,
            'order_item': order_item,
            'order_totals': order_totals,
        }

        return render(request, 'shop/checkout.html', context)


    def post(self, request, *args, **kwargs):
        pass
