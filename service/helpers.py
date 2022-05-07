from django.shortcuts import get_object_or_404
from .models import Category


def barber_list_filter_sort(request, barbers,  category_slug=None):
    is_sort_asc = request.GET.get('price')
    is_sort_desc = request.GET.get('-price')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        barbers = barbers.filter(category=category)
    if is_sort_asc:
        barbers = barbers.order_by('price')
    elif is_sort_desc:
        barbers = barbers.order_by('-price')
    return barbers