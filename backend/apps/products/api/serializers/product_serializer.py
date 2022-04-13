from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasurUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    ''' PRIMER METODO PARA DATOS DE UNA LLAVE FORANEA CON AYUDA DE SERIALIZADORES '''
    # measure_unit = MeasurUnitSerializer()
    # category_product = CategoryProductSerializer()

    ''' SEGUNDO METODO PARA MOSTRAR DATOS DE UNA LLAVE FORANEA MEDIANTE EL METODO __str__ DEL MODEL '''
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state',)

    ''' TERCER METODO PARA MOSTRAR DATOS DE UNA LLAVE FORANEA MEDIANTE EL METODO to_representation'''

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'image': instance.image if instance.image != '' else '',
            'description': instance.description,
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else '',
        }
