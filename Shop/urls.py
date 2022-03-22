from django.urls import path
from Shop import views

app_name= 'Shop'
urlpatterns = [
    path('', views.ProductList.as_view(), name="home"),
    path('product/<slug:slug>/', views.product_details, name="product_details"),
]
