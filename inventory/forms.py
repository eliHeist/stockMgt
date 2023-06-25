from django.forms import ModelForm

from inventory.models import Product


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'