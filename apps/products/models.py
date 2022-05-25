from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

# Create your models here.


class MeasureUnit(BaseModel):
    description = models.CharField(
        "Descripción", max_length=50, blank=False, null=False, unique=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medidas"

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):
    description = models.CharField(
        "Descripción", max_length=50, blank=False, null=False, unique=True
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de producto"
        verbose_name_plural = "Categorias de productos"

    def __str__(self):
        return self.description


class Product(BaseModel):
    name = models.CharField(
        "Nombre de producto", max_length=150, unique=True, blank=False, null=False
    )
    description = models.TextField("Descripción de producto", blank=False, null=False)
    image = models.ImageField("Imagen del producto", upload_to="products/", blank=True, null=True)
    measure_unit = models.ForeignKey(
        MeasureUnit,
        verbose_name="Unidad de medida",
        on_delete=models.CASCADE,
        null=True,
    )
    category_product = models.ForeignKey(
        CategoryProduct(),
        verbose_name="Categoria de producto",
        on_delete=models.CASCADE,
        null=True,
    )
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
