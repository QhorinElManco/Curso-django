from rest_framework import routers
from apps.products.api.views.product_viewset import ProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='Productos')

urlpatterns = router.urls