from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializer import UserSerializer, UserListSerializer


""" METODOS COMO CLASE """
"""class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
"""

""" METODO COMO FUNCION Y DECORADOR """


@api_view(["GET", "POST", "DELETE", "PUT"])
def user_api_view(request):
    # List
    if request.method == "GET":
        # Queryset
        # Optimizando consulta solo con los datos que necesitamos para esto
        # debemos configurar los campos en el serializer
        users = User.objects.all().values("id", "username", "email", "password")
        # users = User.objects.all()
        users_serializer = UserListSerializer(users, many=True)

        """ VALIDACIONES PERSONALIZADAS DE SERIALIZER """
        """
        
        EJEMPLO PRACTICO DE METODO CREATE DE UN SERIALIZADOR CUANDO NO ESTA BASADO EN UN MODELO

        test_data = {
            'name': 'develop',
            'email': 'test@gmail.com'
        }

        test_user = TestUserSerializer(data=test_data, context=test_data)

        if test_user.is_valid():
            user_instance = test_user.save()
        print(test_user.errors)
        
        """

        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # Create
    elif request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        # Validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {
                    "message": "Usuario creado correctamente",
                    "data": user_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(request, pk=None):
    # Queryset
    user = User.objects.filter(id=pk).first()

    if user:

        # Retrieve
        if request.method == "GET":
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # Update
        elif request.method == "PUT":
            user_serializer = UserSerializer(user, request.data)
            # user_serializer = TestUserSerializer(user, request.data)

            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

        # Delete
        elif request.method == "DELETE":
            user.delete()
            return Response(
                {"message": "Eliminado correctamente"}, status=status.HTTP_200_OK
            )
    return Response(
        {"message": "No se ha encontrado un usuarios con estos datos"},
        status=status.HTTP_404_NOT_FOUND,
    )
