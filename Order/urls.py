from django.urls import path
from Order import views

app_name = 'Order'

urlpatterns = [
    path('add-cart/<int:pk>/', views.add_to_cart, name='add-cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase-quantity/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('decrease-quantity/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),
]
