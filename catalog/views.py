from django.http import request, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm


class ProductView(ListView):
    model = Product
    template = 'catalog/home'


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactView(View):
    template_name = "catalog/contacts.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # будет использовано позднее
        return render(request, 'catalog/not_available.html')
