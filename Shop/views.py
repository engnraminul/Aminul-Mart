from django.shortcuts import render

from django.views.generic import ListView, DetailView
from Shop.models import Category, Product


class ProductList(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'


# def product_details(request, pk):
#     product = Product.objects.get(id=pk)
#     context={
#         'product': product
#     }
#     return render(request, 'Shop/product.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'
