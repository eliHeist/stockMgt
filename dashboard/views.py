from django.shortcuts import render
from django.views.generic import TemplateView
from inventory.models import Product

from orders.models import Order

# Create your views here.

class HomepageView(TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['order_count'] = Order.objects.count()
        context['product_count'] = Product.objects.count()
        context['no_stock_product_count'] = Product.objects.filter(quantity=0).count()
        return context
    
