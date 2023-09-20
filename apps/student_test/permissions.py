from django.utils import timezone
from rest_framework import permissions
from apps.student_test.models import UserTest, UserAnswer


class IsHasAccessToDetailOfQuestion(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        current_time = timezone.now()
        test = obj.test
        if test:
            user_test = UserTest.objects.filter(
                user=request.user.id,
                test=test.id,
                end_time__gte=current_time,
                is_finished=False,
            ).first()
            if user_test and request.method in permissions.SAFE_METHODS:
                return True


class IsHasAccessToUserAnswer(permissions.BasePermission):
    def has_permission(self, request, view):
        current_time = timezone.now()
        user_test_id = request.data.get("user_test")
        if user_test_id:
            user_test = UserTest.objects.filter(
                user=request.user.id,
                id=user_test_id,
                end_time__gte=current_time,
                is_finished=False,
            ).first()
            if user_test and request.method in ("POST",):
                return True


class IsHasAccessToUserAnswerUpdate(permissions.BasePermission):
    def has_permission(self, request, view):
        current_time = timezone.now()
        user_test_id = request.data.get("user_test")
        question = request.data.get("question")
        if user_test_id:
            user_answer = UserAnswer.objects.filter(
                user_test__user=request.user.id,
                user_test=user_test_id,
                user_test__end_time__gte=current_time,
                user_test__is_finished=False,
                question=question,
            ).first()
            if user_answer and request.method in ("PUT",):
                return True
