from django.shortcuts import render

from django.views.generic import ListView, DetailView
from Shop.models import Category, Product


class ProductList(ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'
