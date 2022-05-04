from django.shortcuts import render


def get_products_list(request):
    return render(request, 'shop.html')

