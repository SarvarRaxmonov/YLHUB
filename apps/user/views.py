from django.contrib.auth.models import User
from rest_framework import generics

from apps.user.serializers import UserRegisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
