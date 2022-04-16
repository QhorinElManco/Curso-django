from datetime import datetime
from django.contrib.sessions.models import Session
from django.forms import all_valid
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializer import UserTokenSerializer


class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get("username")
        try:
            user_token = Token.objects.get(
                user=UserTokenSerializer()
                .Meta.model.objects.filter(username=username)
                .first()
            )
            return Response({"token": user_token.key}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "Credenciales enviadas son incorrectas"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response(
                        {
                            "token": token.key,
                            "user": user_serializer.data,
                            "message": "Token creado exitosamente",
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:

                    # CASO DE USO BORRAR SESIONES #
                    """Si inicia sesión en otro dispositivo o pestaña cierra las sesiones activas"""
                    """
                    all_sessions = Session.objects.filter(
                        expire_date__gte=datetime.now()
                    )
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response(
                        {
                            "token": token.key,
                            "user": user_serializer.data,
                            "message": "Token creado exitosamente",
                        },
                        status=status.HTTP_201_CREATED,
                    )"""

                    # CASO DE USO DE SESIONES #
                    """ No deja iniciar sesión en caso de que ya haya una sesión abierta """
                    return Response(
                        {"Error": "Ya hay una sesión iniciada con este usuario"},
                        status=status.HTTP_409_CONFLICT,
                    )
            else:
                return Response(
                    {"message": "Este usuario no puede iniciar sesión"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {
                    "message": "Verifica que el nombre de usuario y/o contraseña estén correctos"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class Logout(APIView):
    def post(self, request, *args, **kwargs):
        token = request.POST.get("token")
        token = Token.objects.filter(key=token).first()

        if token:
            user = token.user
            all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
            if all_sessions.exists():
                for session in all_sessions:
                    session_data = session.get_decoded()
                    if user.id == int(session_data.get("_auth_user_id")):
                        session.delete()

            token.delete()
            session_message = "Sessiones de usuario eliminadas"
            token_message = "Token eliminado"
            return Response(
                {
                    "session_message": session_message,
                    "token_message": token_message,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "No se ha encontrado un usuario con estas credenciales"},
            status=status.HTTP_400_BAD_REQUEST,
        )
