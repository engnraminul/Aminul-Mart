from django.contrib import admin
from Shop.models import Category, Brand, Product, ProductImageGallery


class GalleryImageAdmin(admin.StackedInline):
    model = ProductImageGallery

class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryImageAdmin] #product add page show gallery omagge add system
    prepopulated_fields = {'slug': ('product_name',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
