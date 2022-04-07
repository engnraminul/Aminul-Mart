from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from Shop.models import Category, Product, ProductImageGallery, Banner


class ProductList(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        banners = Banner.objects.filter(banner_active=True).order_by('-id')[0:2]

        context = {
            'products':products,
            'banners':banners,
        }
        return render(request, 'Shop/home.html', context)

    def post(self, request, *args, **kwargs):
         if request.method =='POST' or request.method == 'post':
             search_product = request.POST.get('search_product')
             products = Product.objects.filter(product_name__icontains=search_product).order_by('-id')

             context = {
                'products':products,
             }
             return render(request, 'Shop/home.html', context)



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
