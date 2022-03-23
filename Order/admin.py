from django.contrib import admin
from Order.models import Cart, CartToOrder
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartToOrder)
