from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=80, blank=False, null=False)
    category_image = models.ImageField(upload_to='category', blank=True, null=True)
    category_parent = models.ForeignKey('self', related_name='category_children', on_delete=models.CASCADE, blank=True, null=True)
    category_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['-category_name']
        verbose_name_plural = 'Categories'

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, blank=False, null=False)
    brand_image = models.ImageField(upload_to='brand', blank=True, null=True)
    brand_category = models.ForeignKey('Category', related_name='brand_category', on_delete=models.CASCADE, blank=True, null=True)
    brand_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        ordering = ['-brand_name']
        verbose_name_plural = 'Brands'


class Product(models.Model):
    product_name = models.CharField(max_length=264, blank=False, null=False)
    product_brand = models.ForeignKey('Brand', related_name='Product_brand', on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, blank=True, null=True)
    product_description = models.TextField(max_length=2000, blank=True, null=True)
    product_image = models.ImageField(upload_to='products', blank=False, null=False)
    product_price = models.FloatField()
    product_old_price = models.FloatField(default=0.00, blank=True, null=True)
    Product_stock = models.BooleanField(default=True)
    product_created = models.DateTimeField(auto_now_add=True)
    product_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-product_created']

    #custom slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)

    def product_url(self):
        return reverse('Shop:product_details', kwargs={'slug':self.slug})



class ProductImageGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    gallery_image = models.FileField(upload_to='Image_gallery')
    gallery_created = models.DateTimeField(auto_now_add=True)


class VariationManager(models.Manager):
    def variants(self):
        return super(VariationManager, self).filter(variation='variant')

    def colors(self):
        return super(VariationManager, self).filter(variation='color')


VARIATIONS_TYPE = (
    ('variant', 'variant'),
    ('color', 'color'),
)

class VariationValue(models.Model):
    variation = models.CharField(max_length=100, choices=VARIATIONS_TYPE)
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.name
class Banner(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banner')
    banner_image = models.ImageField(upload_to='banner')
    banner_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.product_name

class Logo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logo')
    active_logo = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.logo)

class FavIcon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='logo')
    active_icon = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.icon)
