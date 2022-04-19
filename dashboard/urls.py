from django.urls import path
from dashboard import views


app_name= 'dashboard'
urlpatterns = [
    path('index/', views.DashboardIndex.as_view(), name='dashboard_index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('add-new-product/', views.AddNewProduct.as_view(), name='add_new_product'),
    path('product-update/<slug:slug>/', views.ProductUpdate.as_view(), name='product_update'),
    path('product-delete/<slug:slug>/', views.ProductDelete.as_view(), name='product_delete'),
    path('category/', views.CategoryList.as_view(), name = 'category_list'),
    path('add-new-category/', views.AddNewCategory.as_view(), name= 'add_new_category'),
]
