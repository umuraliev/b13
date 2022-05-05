from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_product_list, name='products_list'),
    path('search_product/', views.search_product, name='search'),
    path('<str:category_slug>/', views.get_product_list, name='product_list_by_category'),
]
