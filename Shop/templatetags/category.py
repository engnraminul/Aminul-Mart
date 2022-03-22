from django import template
from Shop.models import Category

register = template.Library()

@register.filter
def category(user):
    if user.is_authenticated:
        categorys = Category.objects.filter(category_parent=None)
        return categorys
