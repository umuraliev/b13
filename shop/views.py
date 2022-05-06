from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator

from cart.forms import CartAddProductForm
from .helpers import product_list_filter_sort
from .models import Category, Product
from .forms import ProductForm
from django.db.models import Q
from django.conf import settings

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


def get_product_detail(request, product_slug):
    """Детализация продукта
    """
    product = get_object_or_404(Product, slug=product_slug)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(
        request, 'product_detail.html', context
    )



def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('products_list')
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'product_form': form})


def delete_product(request, product_slug):
    Product.objects.get(slug=product_slug).delete()
    return redirect('/')
