from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('history/', views.order_history, name='order-history'),
    path('history/detail/<int:order_id>/',views.order_history_detail, name='order-detail'),
]