from django.urls import path

from api.views import productApiView

app_name = 'api'

urlpatterns = [
    path('products/', productApiView, name='products'),
]