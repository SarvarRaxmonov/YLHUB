from django.urls import path

from .views import ContentAPIView, ContentDetailAPIView, CreateChoiceAPIView

urlpatterns = [
    path("contents/", ContentAPIView.as_view(), name="contents"),
    path(
        "contents/<str:model_type>/<int:pk>/",
        ContentDetailAPIView.as_view(),
        name="content-detail",
    ),
    path(
        "contents/poll/choice/<int:pk>/create/",
        CreateChoiceAPIView.as_view(),
        name="create-choice",
    ),
]
