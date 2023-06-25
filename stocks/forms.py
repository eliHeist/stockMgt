from django import forms

from stocks.models import Batch, Stock


class BatchModelForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'
        widgets = {
            'product': forms.TextInput(attrs={'list': 'product_datalist'}),
        }


class StockModelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
    
BatchFormSet = forms.inlineformset_factory(Stock, Batch, form=BatchModelForm, extra=1)
