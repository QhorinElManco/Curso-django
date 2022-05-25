from django.shortcuts import get_object_or_404
from rest_framework import status

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.api.serializer import (
    UserListSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
from apps.users.models import User


class UserViewSet(GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = (
                self.serializer_class()
                .Meta.model.objects.filter(is_active=True)
                .values("id", "username", "email", "name", "last_name")
            )
        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED)
        return Response(
            {"message": "Error al guardar usuario", "error": user_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UserUpdateSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {"message": "Usuario actualizado correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "El usuario no se ha actualizado",
                "errors": user_serializer.errors,
            },
            status=status.HTTP_304_NOT_MODIFIED,
        )

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response(
                {"message": "Usuario eliminado correctamente"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "El usuario no ha sido encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
