from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .helpers import product_list_filter_sort
from .models import Category, Product
from .forms import ProductForm
from django.db.models import Q
from django.conf import settings
# from cart.forms import CartAddProductForm

def search_product(request):
    category = None
    categories = Category.objects.all()
    products = None
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(
                               Q(name__icontains=search) |
                               Q(description__icontains=search))
    context = {
        'products': products,
        'categories': categories,
        'category': category
    }
    return render(
                  request,
                  'shop.html',
                  context
    )

def get_product_list(request, category_slug=None):
    """
    Функция вытаскивает продукты и если слаг приходит заполненным,
    то фильтрует по слагу и в конце вовращаем контексты
    """

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('created_at')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # фильтрация по прайс и категориям
    products = product_list_filter_sort(
        request,
        products,
        category_slug
    )
    paginator = Paginator(products, settings.PAGINATOR_NUM)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)


    context = {
        'products': products,
        'categories': categories,
        'category': category,
    }
    return render(
        request,
        'shop.html',
        context=context
    )

