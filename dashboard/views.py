from django.shortcuts import render
from django.views.generic import TemplateView

from Shop.models import Product

class DashboardIndex (TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/index.html')

    def post(self, request, *args, **kwargs):
        pass



class ProductListView(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by('-id')
        context = {
            'products': products
        }
        return render(request, 'dashboard/product_list.html', context)

    def post(self, request, *args, **kwargs):
        pass
