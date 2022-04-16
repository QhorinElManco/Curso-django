from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.products.api.serializers.product_serializer import ProductSerializer
from apps.users.authentication_mixins import Authentication

'''"ms-python.python"'''


class ProductViewSet(Authentication, viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return (
                self.get_serializer()
                .Meta.model.objects.filter(state=True, id=pk)
                .first()
            )

    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Producto creado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data
            )
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(
                product_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"message": "El producto con estos datos no existe"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response(
                {"message": "Producto eliminado correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "El producto con estos datos no existe"},
            status=status.HTTP_404_NOT_FOUND,
        )
