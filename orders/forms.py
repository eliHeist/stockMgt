from django.forms import ModelForm, inlineformset_factory, DateTimeInput, TextInput

from orders.models import Order, OrderItem

class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'date': DateTimeInput(attrs={'type': 'date'}),
        }


class OrderItemModelForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
        widgets = {
            'product': TextInput(attrs={'list': 'product_datalist'}),
        }
    
OrderItemFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemModelForm, extra=1)
