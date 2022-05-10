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
    # comments = barbers.comments.filter(active=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        barbers = barbers.filter(category=category)
        barbers = barber_list_filter_sort(
            request,
            barbers,
            category_slug
        )

    # if request.method == 'POST':
    #     # A comment was posted
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         # Create Comment object but don't save to database yet
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.barbers = barbers
    #         # Save the comment to the database
    #         new_comment.save()
    # else:
    #     comment_form = CommentForm()

    paginator = Paginator(barbers, settings.PAGINATOR_NUM)
    page_number = request.GET.get('page')
    barbers = paginator.get_page(page_number)

    context = {
        'barbers': barbers,
        'category': category,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(
        request,
        'barbers_list.html',
        context=context
    )






list = []
@login_required()
def entries_time(request):
    if request.method == "POST":
        form = EntriesForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            data = form.cleaned_data
            list.append(data['date'])
            print(list)
                # raise ValidationError('Это время уже занято')
            obj.user = request.user
            obj.save()
    form = EntriesForm()
    return render(request, 'entries.html', {'form': form})




# print(form.cleaned_data)



