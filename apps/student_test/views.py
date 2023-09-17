from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from apps.student_test.models import Test, UserTest
from apps.student_test.serializers import TestSerializer, UserTestSerializer


class TestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class UserTestViewSet(CreateAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
