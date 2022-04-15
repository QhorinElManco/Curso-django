from datetime import datetime
from django.contrib.sessions.models import Session
from django.forms import all_valid
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializer import UserTokenSerializer


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
                    '''all_sessions = Session.objects.filter(
                        expire_date__gte=datetime.now()
                    )
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decode()
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
                    )'''

                    # CASO DE USO DE SESIONES #
                    """ No deja iniciar sesión en caso de que ya haya una sesión abierta """
                    return Response({'Error':'Ya hay una sesión iniciada con este usuario'}, status = status.HTTP_409_CONFLICT)
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
