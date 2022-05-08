from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def get_main(request):
    return render(request, 'index.html')



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "base.html" 
    