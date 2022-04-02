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

        context = {
            'billingaddress': form,
        }

        return render(request, 'shop/checkout.html', context)


    def post(self, request, *args, **kwargs):
        pass
