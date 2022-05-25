from rest_framework import routers

from apps.products.api.views.general_viewset import (
    CategoryProductViewSet,
    MeasureUnitViewSet,
)
from apps.products.api.views.product_viewset import ProductViewSet

router = routers.DefaultRouter()

router.register(r"products", ProductViewSet, basename="Productos")
router.register(r"categorys", CategoryProductViewSet, basename="Categorias")
router.register(r"measure-unit", MeasureUnitViewSet, basename="Productos")

urlpatterns = router.urls
