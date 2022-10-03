import jwt

from rest_framework import authentication, exceptions
from django.conf import settings

from api.user.models import User
from api.authentication.models import ActiveSession


class ActiveSessionAuthentication(authentication.BaseAuthentication):

    auth_error_message = {"success": False, "msg": "User is not logged on."}

    def authenticate(self, request):

        request.user = None

        auth_header = authentication.get_authorization_header(request)

        if not auth_header:
            return None

        token = auth_header.decode("utf-8")

        return self._authenticate_credentials(token)

    def _authenticate_credentials(self, token):

        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed(self.auth_error_message)

        try:
            active_session = ActiveSession.objects.get(token=token)
        except:
            raise exceptions.AuthenticationFailed(self.auth_error_message)

        try:
            user = active_session.user
        except User.DoesNotExist:
            msg = {"success": False, "msg": "No user matching this token was found."}
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = {"success": False, "msg": "This user has been deactivated."}
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
