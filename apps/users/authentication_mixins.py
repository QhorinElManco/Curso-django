from rest_framework import authentication, exceptions, status
from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.users.authentication import ExpiredTokenAuthentication


class Authentication(authentication.BaseAuthentication):

    user = None

    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()

            except exceptions:
                return None

            token_expire = ExpiredTokenAuthentication()

            user = token_expire.authenticate_credentials(token)

            if user is not None:
                self.user = user
                return user
        return None

    """EL METODO AUTENTICATE QUE SE HEREDA DE authentication.BaseAuthentication
    AL UTILIZAR UN AUTHENTICATION CUSTOM SIEMPRE DEBE SER SOBREESCRITO"""

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailde("No se han enviado las credenciales")
        return (self.user, None)

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is not None:
            return super().dispatch(request, *args, **kwargs)
        response = Response(
            {"error": "No se han enviado las credenciales"},
            status=status.HTTP_400_BAD_REQUEST,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response
