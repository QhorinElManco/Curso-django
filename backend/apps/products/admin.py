from django.contrib import admin
from apps.products.models import Product, CategoryProduct, MeasureUnit

# Modify fields of your models


@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


# Register your models here.
# admin.site.register(MeasureUnit)
# admin.site.register(CategoryProduct)
admin.site.register(Product)
