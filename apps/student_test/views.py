from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from apps.student_test.permissions import (
    IsHasAccessToDetailOfQuestion,
    IsHasAccessToUserAnswer,
    IsHasAccessToUserAnswerUpdate,
)
from apps.student_test.models import Test, UserTest, TestQuestion, UserAnswer
from apps.student_test.serializers import (
    TestSerializer,
    UserTestSerializer,
    TestQuestionSerializer,
    UserAnswerSerializer,
)


class TestDetailViewSet(RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestQuestionDetailViewSet(RetrieveAPIView):
    queryset = TestQuestion
    serializer_class = TestQuestionSerializer
    permission_classes = (IsHasAccessToDetailOfQuestion,)


class UserTestCreateViewSet(CreateAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer


class UserAnswerCreateViewSet(CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = (IsHasAccessToUserAnswer,)


class UserAnswerUpdateViewSet(UpdateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = (IsHasAccessToUserAnswerUpdate,)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return
