from rest_framework import generics, status
from rest_framework.response import Response

# from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializer import ProductSerializer

"""
    :TODO
    Manejar los metodos http con viewsets en el archivo product_viewset.py
"""


"""
# List API
class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

# Create API
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Producto creado correctamente'},
                status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
""" LIST AND CREATE TOGETHER
Unificar vistas de post y get en en una sola
"""

# List and Create API


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    # queryset = ProductSerializer.Meta.model.objects.filter(state = True)

    # Los más recomendable es utilizar la función get_queryset
    # por temas de validación y escalabilidad
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Producto creado correctamente"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
# Retrieve API
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

# Update/Patch API
class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'message': 'El producto con estos datos no existe'},
            status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {'message': 'El producto con estos datos no existe'},
            status=status.HTTP_404_NOT_FOUND
            )
"""


# Retrieve, Update and Destroy API
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(state=True, id=pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"message": "El producto con estos datos no existe"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"message": "El producto con estos datos no existe"},
            status=status.HTTP_404_NOT_FOUND,
        )

    def delete(self, request, pk=None):
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


"""
# Delete API
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response(
                {'message': 'Producto eliminado correctamente'},
                status=status.
                )
        return Response({'message': 'El producto con estos datos no existe'}
        , status=status.HTTP_404_NOT_FOUND
        )
"""

"""
Vistas basadas en clases:
    ListCreateAPIView
    RetrieveUpdate
    RetrieveDestroy
    RetrieveUpdateDestroy
"""
