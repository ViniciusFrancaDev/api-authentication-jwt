from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .services.authentication import (
    create_authentication_token,
    decode_authentication_token,
)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        user = User.objects.filter(email=request.data["email"]).first()

        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        if not user.check_password(request.data["password"]):
            raise AuthenticationFailed("Invalid credentials")

        access_token = create_authentication_token(user.id)
        refresh_token = create_authentication_token(user.id, "refresh_secret", 3600)

        response = Response()
        response.set_cookie(key="refreshToken", value=refresh_token, httponly=True)
        response.data = {"access_token": access_token}

        return response


class UserView(APIView):
    def get(self, request):
        authorization_header = get_authorization_header(request).split()

        if authorization_header is None or len(authorization_header) != 2:
            raise AuthenticationFailed("Unauthenticated")

        token = authorization_header[1].decode("utf-8")
        user_id = decode_authentication_token(token)

        user = User.objects.filter(pk=user_id).first()

        return Response(UserSerializer(user).data)


class LogoutView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie("refreshToken")
        response.data = {"message": "success"}

        return response


class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refreshToken")
        user_id = decode_authentication_token(refresh_token, "refresh_secret")

        access_token = create_authentication_token(user_id)

        return Response({"access_token": access_token})
