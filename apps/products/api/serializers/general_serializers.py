from rest_framework import serializers

from apps.products.models import CategoryProduct, MeasureUnit


class MeasurUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = ("id", "description")
        # exclude = ('state',)


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ("state",)
