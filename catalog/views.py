from django.http import request, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, View



class ProductView(ListView):
    model = Product
    template = 'catalog/home'


class ProductDetailView(DetailView):
    model = Product


class HttpResonseRedirect:
    pass


class ContactView(View):
    template_name = "catalog/contacts.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # будет использовано позднее
        return render(request, 'catalog/not_available.html')
