from django.urls import path

from apps.student_test.views import (
    TestDetailViewSet,
    UserTestCreateViewSet,
    TestQuestionDetailViewSet,
    UserAnswerCreateViewSet,
    UserAnswerUpdateViewSet,
    UserTestFinishAPIView,
    UserTestResultViewSet,
)

urlpatterns = [
    path("test-detail/<int:pk>", TestDetailViewSet.as_view(), name="test-detail"),
    path(
        "test-question-detail/<int:pk>",
        TestQuestionDetailViewSet.as_view(),
        name="test-question-detail",
    ),
    path("start-test/", UserTestCreateViewSet.as_view(), name="start-test"),
    path("answer/", UserAnswerCreateViewSet.as_view(), name="answer"),
    path(
        "answer-update/<int:pk>",
        UserAnswerUpdateViewSet.as_view(),
        name="answer-update",
    ),
    path(
        "finish-test/<int:user_test_id>",
        UserTestFinishAPIView.as_view(),
        name="finish-test",
    ),
    path(
        "result-test/<int:id>",
        UserTestResultViewSet.as_view(),
        name="result-test",
    ),
]
