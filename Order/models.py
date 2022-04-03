from django.db import models

from django.conf import settings
from Shop.models import Product, VariationValue


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    variant = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.item}"


    def get_total_price(self):
        total = self.item.product_price * self.quantity
        float_total_price = format(total, '0.2f')
        return float_total_price


    def single_variation_price(self):
        variants = VariationValue.objects.filter(variation='variant', product=self.item)
        colors = VariationValue.objects.filter(variation='color',  product=self.item)
        colors_price=0
        for variant in variants:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        colors_price = color.price
                if variant.name == self.variant:
                    total = variant.price + colors_price
                    net_total = total
                    float_total = format(net_total, '0.2f')
                    return float_total
            else:
                if variant.name == self.variant:
                    total = variant.price
                    float_total = format(total, '0.2f')
                    return float_total

    def variation_total(self):
        variants = VariationValue.objects.filter(variation='variant', product=self.item)
        colors = VariationValue.objects.filter(variation='color',  product=self.item)
        for variant in variants:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        color_price = color.price
                        color_quantity_price = color_price * self.quantity
                if variant.name == self.variant:
                    total = variant.price * self.quantity
                    net_total = total + color_quantity_price
                    float_total = format(net_total, '0.2f')
                    return float_total
            else:
                if variant.name == self.variant:
                    total = variant.price * self.quantity
                    float_total = format(total, '0.2f')
                    return float_total



class CartToOrder(models.Model):
    PAYMENT_METHOD = (
        ('Cash on Delivery', 'Cash on Delivery'),
        ('PayPal', 'PayPal'),
        ('SSLcommerz', 'SSLcommerz'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=250, blank=True, null=True)
    orderId = models.CharField(max_length=250, blank=True, null=True)
    payment_method = models.CharField(max_length=40, choices=PAYMENT_METHOD, default='Cash on Delivery')

    def get_totals_price(self):
        total=0
        for order_item in self.orderitems.all():
            if order_item.variation_total():
                total +=float(order_item.variation_total())
            elif order_item.single_variation_price():
                total +=float(order_item.single_variation_price())
            else:
                total +=float(order_item.get_total_price())
        return total
