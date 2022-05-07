from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_services_list, name='services_list'),
    path('<str:category_slug>/', views.get_barbers_list, name='barber_list_by_category'),
]