from rest_framework.views import Response
from rest_framework.decorators import api_view

from api.serializers import ProductSerializer
from inventory.models import Product


@api_view(['GET'])
def productApiView(request, pk=None):
    context = {}
    if not pk and request.method == 'GET':
        products = Product.objects.all()
            
        serializer = ProductSerializer(products, many=True)
    
        context['status'] = 200
        context['data'] = serializer.data

        
    return Response(context)
