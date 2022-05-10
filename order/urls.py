from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.checkout_page, name='order_create'),
    path('history/', views.order_history, name='order-history'),
    path('payment/', views.payment, name='payment'),
    path('history/detail/<int:order_id>/',views.order_history_detail, name='order-detail'),
    path('cash/', views.OrderCreateView.as_view(), name='cash_order'),
    
]