from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Service, Category


class MainView(ListView):
    # Список категорий
    model = Category
    queryset = Category.objects.all()
    template_name = "services/index.html"

class ContactView(View):
    def get(self, request):
        return render(request, "services/contact.html")


class ServiceListView(ListView):
    # Список услуг
    model = Service
    slug_field = "url"


class ServiceDetailView(DetailView):
    # Информация об услуге
    model = Service
    slug_field = "url"
