from rest_framework import viewsets
from rest_framework.response import Response
from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    # queryset = Product.objects.all()
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True) 
    