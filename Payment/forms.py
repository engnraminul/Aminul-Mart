from django import forms
form Payment.models import BillingAddress

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fiels = ['name', 'address', 'city', 'country', 'zipcode', 'phone']
