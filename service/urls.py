from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_services_list, name='services_list'),

]