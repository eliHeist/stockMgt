from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from inventory.forms import ProductModelForm

from inventory.models import Product

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "inventory/product-list.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = "inventory/product-create.html"
    success_url = 'inventory:product-list'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = "inventory/product-update.html"
    success_url = 'inventory:product-list'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "inventory/product-delete.html"
    success_url = 'inventory:product-list'
