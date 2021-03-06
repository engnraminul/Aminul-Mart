from django import forms
from Payment.models import BillingAddress
from django.db.models import fields
from Order.models import CartToOrder

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['name','address','city','country','zipcode','phone']

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = CartToOrder
        fields = ['payment_method']
