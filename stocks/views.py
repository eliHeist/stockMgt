from typing import Any, Dict
from django.shortcuts import redirect, render

from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from inventory.models import Product
from stocks.forms import BatchFormSet, StockModelForm

from stocks.models import Stock

# Create your views here.
class StockListView(ListView):
    model = Stock
    template_name = "stocks/stock-list.html"


class StockCreateView(CreateView):
    model = Stock
    form_class = StockModelForm
    template_name = "stocks/stock-create.html"
    success_url = 'stocks:stock-list'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['batch_formset'] = BatchFormSet(self.request.POST, prefix='batches')
        else:
            context['products'] = Product.objects.filter(quantity__gte=1)
            context['batch_formset'] = BatchFormSet(prefix='batches')
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        batch_formset = context['batch_formset']
        print(batch_formset)
        if not batch_formset.is_valid():
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()
        batch_formset.instance = self.object
        print(batch_formset)
        batch_formset.save()

        batches = batch_formset.save(commit=False)
        print(batches)
        for batch in batches:
            print(batch)
            batch.product.quantity = int(batch.product.quantity) + int(batch.quantity)
            batch.product.save()
        return redirect(self.get_success_url())


class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockModelForm
    template_name = "stocks/stock-update.html"
    success_url = 'stocks:stock-list'


class StockDeleteView(DeleteView):
    model = Stock
    template_name = "stocks/stock-delete.html"
    success_url = 'stocks:stock-list'


class StockDetailView(DetailView):
    model = Stock
    context_object_name = 'stock'
    template_name = "stocks/stock-detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['batch_formset'] = BatchFormSet(self.request.POST, prefix='batches')
        else:
            context['products'] = Product.objects.filter(quantity__gte=1)
            context['batch_formset'] = BatchFormSet(prefix='batches')
            context['stock'] = self.object
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        batch_formset = context['batch_formset']
        if not batch_formset.is_valid():
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()
        batch_formset.instance = self.object
        batch_formset.save()
        return redirect(self.get_success_url())