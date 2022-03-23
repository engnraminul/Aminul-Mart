from django.db import models

from django.conf import settings
from Shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.item}"


    def get_total_price(self):
        total = self.item.product_price * self.quantity
        float_total_price = format(total, '0.2f')
        return float_total_price


class CartToOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=250, blank=True, null=True)
    orderId = models.CharField(max_length=250, blank=True, null=True)

    def get_totals_price(self):
        total=0
        for order_item in self.orderitems.all():
            total +=float(order_item.get_total_price())
        return total
