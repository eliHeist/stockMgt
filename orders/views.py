from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DetailView
from inventory.models import Product
from orders.forms import OrderItemFormSet, OrderModelForm

from orders.models import Order

# Create your views here.
class OrderListView(ListView):
    model = Order
    template_name = "orders/order-list.html"


class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = "orders/order-detail.html"


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderModelForm
    template_name = "orders/order-create.html"
    success_url = 'orders:order-list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['orderitem_formset'] = OrderItemFormSet(self.request.POST, prefix='orderitemes')
        else:
            context['products'] = Product.objects.filter(quantity__gte=1)
            context['orderitem_formset'] = OrderItemFormSet(prefix='orderitemes')
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        orderitem_formset = context['orderitem_formset']
        print(orderitem_formset)
        if not orderitem_formset.is_valid():
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()
        orderitem_formset.instance = self.object
        print(orderitem_formset)
        orderitem_formset.save()

        orderitemes = orderitem_formset.save(commit=False)
        for orderitem in orderitemes:
            print(orderitem)
            orderitem.product.quantity = int(orderitem.product.quantity) - int(orderitem.quantity)
            orderitem.product.save()
        return redirect(self.get_success_url())