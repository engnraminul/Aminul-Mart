from django.urls import path
from dashboard import views

app_name= 'dashboard'
urlpatterns = [
    path('index/', views.DashboardIndex.as_view(), name='dashboard_index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
]
