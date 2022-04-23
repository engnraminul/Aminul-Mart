from django.forms.models import ModelForm

from Shop.models import Category, Brand, Product, VariationValue, Logo, Banner, FavIcon


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ('slug',)




class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ('__all__')
