from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from Shop.models import Product, Brand, Category
from Shop.forms import ProductForm, CategoryForm

class DashboardIndex (TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/category_list.html')

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

class ProductUpdate(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        form = ProductForm(instance=product)
        context = {
            'form':form
        }
        return render(request, 'dashboard/product_form.html', context)

    def post(self, request, slug, *args, **kwargs):
        if request.user.user_type =='developer':
            if request.method =='post' or request.method == 'POST':
                product = Product.objects.get(slug=slug)
                form = ProductForm(request.POST, request.FILES, instance=product)
                if form.is_valid():
                    product = form.save(commit=False)
                    product_slug = product.product_name.replace(' ', '-')
                    product.slug = product_slug.lower()
                    product.save()
                    return redirect('dashboard:product_list')
            else:
                return redirect('Shop:home')
        else:
            return redirect('Shop:home')


class ProductDelete(TemplateView):
    def get(self, request, slug, *args, **kwargs):
        product = Product.objects.get(slug=slug)
        product.delete()
        return redirect('dashboard:product_list')


class CategoryList(ListView):
    model = Category
    template_name = 'dashboard/category_list.html'
    context_object_name = 'categories'

class AddNewCategory(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'developer':
                form = CategoryForm()
                context = {
                    'form': form
                }
                return render(request, 'dashboard/category_form.html', context)
            else:
                return redirect('Shop:home')
            return redirect('account:profile')
        else:
            return redirect('Shop:home')

    def post(self, request, *args, **kwargs):
        if request.user.user_type =='developer':
            if request.method =='post' or request.method == 'POST':
                form = CategoryForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('dashboard:category_list')
            else:
                return redirect('dashboard:category_list')
        else:
            return redirect('dashboard:category_list')


class CategoryUpdate(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.get(id=pk)
        form = CategoryForm(instance=category)
        context = {
            'form': form
        }
        return render(request, 'dashboard/category_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        category = Category.objects.get(id=pk)
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:category_list')
        else:
            return redirect('dashboard:category_list')

class CategoryDelete(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        category.delete()
        return redirect('dashboard:category_list')
