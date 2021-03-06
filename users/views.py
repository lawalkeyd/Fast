from django.views.generic.base import View
import rest_framework
from .models import Userss
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import UserSerializier, ViewUserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CreateUser(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializier


class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class AdminUserView(generics.ListAPIView):
    queryset = Userss.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ViewUserSerializer
