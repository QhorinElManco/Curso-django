from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasurUnitSerializer, CategoryProductSerializer


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasurUnitSerializer


class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer