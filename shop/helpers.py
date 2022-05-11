from django.shortcuts import get_object_or_404
from .models import Category
from django.db import models
from django.db.models import Sum


def product_list_filter_sort(request, products,  category_slug=None):
    is_sort_asc = request.GET.get('price')
    is_sort_desc = request.GET.get('-price')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if is_sort_asc:
        products = products.order_by('price')
    elif is_sort_desc:
        products = products.order_by('-price')
    return products

 
class LikeDislikeManager(models.Manager):
    use_for_related_fields = True
 
    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def products(self):
        return self.get_queryset().filter(content_type__model='product').order_by('-product__pub_date')