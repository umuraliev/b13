from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_product_list, name='products_list'),
    path('search_product/', views.search_product, name='search'),
]
