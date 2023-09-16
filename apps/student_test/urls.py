from django.urls import path

from .views import TestViewSet

urlpatterns = [
    path("test-detail/<int:pk>", TestViewSet.as_view({"get": "list"}), name="test-detail"),
]
