from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from shop.forms import CommentForm
from .models import *
from django.shortcuts import render, get_object_or_404
from .helpers import barber_list_filter_sort
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import *


def get_services_list(request):
    categories = Category.objects.all()
    return render(request, 'service.html', {'categories': categories})


def get_barbers_list(request, category_slug=None):
    """
    Функция вытаскивает барберов и если слаг приходит заполненным,
    то фильтрует по слагу и в конце вовращаем контексты
    """
    category = None
    barbers = Barber.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        barbers = barbers.filter(category=category)
        barbers = barber_list_filter_sort(
            request,
            barbers,
            category_slug
        )

    paginator = Paginator(barbers, settings.PAGINATOR_NUM)
    page_number = request.GET.get('page')
    barbers = paginator.get_page(page_number)

    context = {
        'barbers': barbers,
        'category': category,
    }
    return render(
        request,
        'barbers_list.html',
        context=context
    )







@login_required()
def entries_time(request):
    if request.method == "POST":
        form = EntriesForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    form = EntriesForm()
    return render(request, 'entries.html', {'form': form})






