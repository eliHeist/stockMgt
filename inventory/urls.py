from django.urls import path

from inventory.views import ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView

app_name = 'inventory'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create', ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
]