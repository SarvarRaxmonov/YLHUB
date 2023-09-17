from django.urls import path

from apps.student_test.views import TestViewSet, UserTestViewSet

urlpatterns = [
    path("test-detail/<int:pk>", TestViewSet.as_view({"get": "list"}), name="test-detail"),
    path("start-test/", UserTestViewSet.as_view(), name="start-test"),
]
