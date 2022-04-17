from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from Shop.models import Product
from Shop.forms import ProductForm

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


class AddNewProduct(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'developer':
                form = ProductForm()
                context = {
                    'form': form
                }
                return render(request, 'dashboard/product_form.html', context)
            else:
                return redirect('Shop:home')
            return redirect('account:profile')
        else:
            return redirect('Shop:home')

    def post(self, request, *args, **kwargs):
        if request.user.user_type =='developer':
            if request.method =='post' or request.method == 'POST':
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    product = form.save(commit=False)
                    product_slug = product.product_name.replace(' ', '-')
                    product.slug = product_slug
                    product.save()
                    return redirect('dashboard:product_list')
            else:
                return redirect('Shop:home')
        else:
            return redirect('Shop:home')
