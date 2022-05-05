from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def get_products_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created_at')
    context = {
        'category':categories,
        'products':products,
    }
    return render(request, 'shop.html', context)