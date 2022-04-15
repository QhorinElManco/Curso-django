from rest_framework import viewsets
from apps.products.api.serializers.general_serializers import MeasurUnitSerializer, CategoryProductSerializer

class CategoryProductViewSet(viewsets.ModelViewSet):

    serializer_class = CategoryProductSerializer
    #queryset = CategoryProduct.objects.all()
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else: 
            return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()
    
class MeasureUnitViewSet(viewsets.ModelViewSet):

    serializer_class = MeasurUnitSerializer
    #queryset = MeasureUnit.objects.all()
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else: 
            return self.get_serializer().Meta.model.objects.filter(state=True,id=pk).first()