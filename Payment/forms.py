from django import forms
from Payment.models import BillingAddress
from django.db.models import fields

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['name','address','city','country','zipcode','phone']
