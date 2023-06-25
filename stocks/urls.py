from django.urls import path

from stocks.views import StockCreateView, StockDeleteView, StockListView, StockUpdateView
from stocks.views import StockDetailView

app_name = 'stocks'

urlpatterns = [
    path('', StockListView.as_view(), name='stock-list'),
    path('create/', StockCreateView.as_view(), name='stock-create'),
    path('update/<int:pk>/', StockUpdateView.as_view(), name='stock-update'),
    path('delete/<int:pk>/', StockDeleteView.as_view(), name='stock-delete'),
    path('detail/<int:pk>/', StockDetailView.as_view(), name='stock-detail'),
]