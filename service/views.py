from django.shortcuts import render


def get_services_list(request):
    return render(request, 'service.html')
    