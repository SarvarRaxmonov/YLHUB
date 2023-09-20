from django.utils import timezone
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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.student_test.utils import temporary_user_point_updater


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


class UserTestResultViewSet(RetrieveAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        point = instance.test.point
        if instance and instance.user_answer_to_user_test.all().filter(is_true=False).exists():
            point = 0
        additional_data = {
            "user": request.user.username,
            "total point": point,
        }
        response_data = {
            **additional_data,
            **serializer.data,
        }
        return Response(response_data)


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


class UserTestFinishAPIView(APIView):

    def post(self, request, user_test_id, *args, **kwargs):
        try:
            current_time = timezone.now().replace(second=0, microsecond=0)
            user_test = UserTest.objects.get(id=user_test_id)
            if (
                user_test.user_answer_to_user_test.all().count()
                == user_test.test.question_to_test.all().count()
                and user_test.end_time > current_time
            ):
                if user_test.user_answer_to_user_test.filter(is_true=False).exists():
                    point = 0
                else:
                    point = user_test.test.point
                    temporary_user_point_updater(request.user.id, point)
                user_test.is_finished = True
                user_test.save()
                return Response(
                    {
                        "user": request.user.username,
                        "user test id": user_test.id,
                        "Right answers count": user_test.user_answer_to_user_test.filter(is_true=True).count(),
                        "total point": point,
                        "is finished": user_test.is_finished
                    },
                    status=status.HTTP_200_OK,
                )
            return Response("You have not finished test or test date is expired")
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
