from django.shortcuts import render

from django.views.generic import ListView, DetailView
from Shop.models import Category, Product, ProductImageGallery, Banner


class ProductList(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['banners'] = Banner.objects.filter(banner_active=True).order_by('-id')[0:2]
        return context

#product details function based

def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    gallery = ProductImageGallery.objects.filter(product=product)
    context={
        'product': product,
        'gallery': gallery,
    }
    return render(request, 'Shop/product.html', context)

#product details class based

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'shop/product.html'
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['gallery'] = ProductImageGallery.objects.filter(product=self.object.id)
#         return context
