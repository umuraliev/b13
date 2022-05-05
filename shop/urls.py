from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_product_list, name='products_list'),
    path('search_product/', views.search_product, name='search'),
    path('add-product/', views.create_product, name='add_product'),
    path('delete/<str:product_slug>/', views.delete_product, name='delete_product'),
    path('<str:category_slug>/', views.get_product_list, name='product_list_by_category'),
    path('products/<str:product_slug>/', views.get_product_detail, name='product_details'),
    
]
