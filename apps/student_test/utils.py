from apps.student_test.models import TestQuestion
from apps.common.models import TemporaryUser
from django.shortcuts import get_object_or_404


def check_answers(question_id, selected_variant):
    if selected_variant:
        question = TestQuestion.objects.get(id=question_id)
        right_answers = list(
            question.variants_to_question.all()
            .order_by("order", "is_true")
            .values_list("id", flat=True)
        )
        if question.type == "choice_order" and right_answers == selected_variant:
            is_true = True
        elif question.type == "multi_select" and set(selected_variant) == set(
            right_answers
        ):
            is_true = True
        elif (
            question.type == "single_select" and selected_variant[0] == right_answers[0]
        ):
            is_true = True
        else:
            is_true = False
        return is_true


def temporary_user_point_updater(user_id: int = None, point: int = 0):
    user = get_object_or_404(TemporaryUser, user__id=user_id)
    user.point += point
    user.save()
