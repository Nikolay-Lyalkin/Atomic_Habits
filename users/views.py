from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializers import UserCreateSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.is_active = True
        new_user.password = make_password(new_user.password)
        new_user.save()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
