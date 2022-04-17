from django.forms.models import ModelForm
from Shop.models import Category, Brand, Product, VariationValue, Logo, Banner, FavIcon


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ('slug',)
