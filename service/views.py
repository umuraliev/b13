from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, render, get_object_or_404
from .helpers import barber_list_filter_sort
from django.conf import settings
from django.core.paginator import Paginator
from shop.forms import CommentForm


def get_services_list(request):
    categories = Category.objects.all()
    return render(request, 'service.html', {'categories': categories})


def get_barbers_list(request, category_slug=None):
    """
    Функция вытаскивает продукты и если слаг приходит заполненным,
    то фильтрует по слагу и в конце вовращаем контексты
    """
    category = None
    barbers = Barber.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        barbers = barbers.filter(category=category)

    # фильтрация по прайс и категориям
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


# def get_barbers_list(request, category_title):
#
#     comments = barber.comments.filter(active=True)
#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.barber = barber
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         'barber': barber,
#         'comments': comments,
#         'comment_form': comment_form
#     }
#     return render(
#         request, 'barber_list.html', context
#     )