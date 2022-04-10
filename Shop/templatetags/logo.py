from django import template

from Shop.models import Logo, FavIcon

register = template.Library()

@register.filter
def logo(request):
    if request:
        logo = Logo.objects.filter(active_logo=True).order_by('-id').first()
        return logo.logo.url
    else:
        logo = Logo.objects.filter(active_logo=True).order_by('-id').first()
        return logo.logo.url

@register.filter
def icon(user):
    if user.is_authenticated:
        icon = FavIcon.objects.filter(user = user, active_icon=True).order_by('-id').first()
        return icon.icon.url
