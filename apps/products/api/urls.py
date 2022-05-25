from django.urls import path

from apps.products.api.views.general_views import (
    CategoryProductListAPIView,
    MeasureUnitListAPIView,
)
from apps.products.api.views.products_views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
)

# from apps.products.api.views.products_views import (
# ProductDestroyAPIView, ProductRetrieveUpdateAPIView)
# from apps.products.api.views.products_views import (
# ProductUpdateAPIView, ProductRetrieveAPIView)
# from apps.products.api.views.products_views import
# (ProductCreateAPIView, ProductListAPIView)

urlpatterns = [
    path("measure_unit/", MeasureUnitListAPIView.as_view(), name="measure_unit"),
    path(
        "category_product/",
        CategoryProductListAPIView.as_view(),
        name="category_product",
    ),
    # path('product/list/', ProductListAPIView.as_view(), name = 'product_list'),
    # path('product/create/', ProductCreateAPIView.as_view(), name = 'product_create'),
    # path(
    # 'product/retrieve/<int:pk>/',
    # ProductRetrieveAPIView.as_view(),
    # name = 'product_retrieve'),
    # path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name = 'product_update'),
    # path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name = 'product_destroy'),
    path("product/", ProductListCreateAPIView.as_view(), name="product_list_create"),
    path(
        "product/retrieve-update-destroy/<int:pk>/",
        ProductRetrieveUpdateDestroyAPIView.as_view(),
        name="product_retrieve_update_destroy",
    ),
]
