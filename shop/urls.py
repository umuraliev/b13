from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products_list, name='products_list'),
]