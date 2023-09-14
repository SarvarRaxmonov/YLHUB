from django.urls import path

from .views import ContentAPIView, ContentDetailAPIView

urlpatterns = [
    path("contents/", ContentAPIView.as_view(), name="contents"),
    path(
        "contents/<str:model_type>/<int:pk>/",
        ContentDetailAPIView.as_view(),
        name="content-detail",
    ),
]
