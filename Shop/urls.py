from django.urls import path
from Shop import views


urlpatterns = [
    path('', views.ProductList.as_view(), name="home"),
]
