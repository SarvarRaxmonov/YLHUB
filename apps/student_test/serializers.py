from datetime import datetime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from apps.student_test.models import Test, UserTest, TestQuestion, Variant, UserAnswer
from apps.student_test.utils import check_answers


class TestQuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ("id", "question", "option")


class TestQuestionSerializer(serializers.ModelSerializer):
    variants_to_question = TestQuestionVariantSerializer(many=True)
    user_answer = serializers.SerializerMethodField()

    class Meta:
        model = TestQuestion
        fields = (
            "id",
            "test",
            "question",
            "type",
            "subject",
            "variants_to_question",
            "user_answer",
        )

    def get_user_answer(self, obj):
        user = self.context["request"].user
        current_time = timezone.now().replace(second=0, microsecond=0)
        answer = UserAnswer.objects.filter(
            user_test__user=user, question=obj.id, user_test__end_time__gte=current_time
        ).first()
        if answer:
            serializer = UserAnswerSerializer(answer)
            return serializer.data
        return


class TestSerializer(serializers.ModelSerializer):
    question_to_test = TestQuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = (
            "id",
            "name",
            "time",
            "resubmit_attempt_count",
            "questions",
            "question_to_test",
        )


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ("id", "test", "start_time", "end_time")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return UserTest.objects.create(**validated_data)

    def validate(self, data):
        current_time = timezone.now().strftime("%Y-%m-%dT%H:%M")
        test = UserTest.objects.filter(
            user=self.context.get("request").user, end_time__gte=current_time
        )
        if test.exists():
            raise ValidationError(
                "You can not do multiple tests at the same time please solve your current test"
            )
        return data

    def validate_test(self, value):
        test = Test.objects.get(id=value.id)
        user_test = (
            UserTest.objects.filter(
                user=self.context.get("request").user, test=test
            ).count()
            - 1
        )
        if user_test >= test.resubmit_attempt_count:
            raise ValidationError(
                "Your attempt count is finished you can not attempt to this test "
            )
        return value

    def validate_start_time(self, value):
        current_time = timezone.now().replace(second=0, microsecond=0)
        if value > current_time or current_time != value:
            raise ValidationError(
                "Start time cannot be in the future or past, it must be in present, now."
            )
        return value

    def validate_end_time(self, value):
        test_taken = Test.objects.get(id=self.initial_data.get("test"))
        start_time = datetime.strptime(
            self.initial_data.get("start_time"), "%Y-%m-%dT%H:%M"
        )
        end_time = datetime.strptime(
            self.initial_data.get("end_time"), "%Y-%m-%dT%H:%M"
        )
        expected_end_time = start_time + test_taken.time
        if end_time != expected_end_time:
            raise ValidationError("Expected right calculated end time for user test.")
        return value


class UserAnswerSerializer(serializers.ModelSerializer):
    is_true = serializers.BooleanField(write_only=False, default=False)

    class Meta:
        model = UserAnswer
        fields = ("id", "user_test", "question", "selected_variant", "is_true")

    def validate(self, obj):
        question = self.initial_data.get("question")
        variants = self.initial_data.get("selected_variant")
        for variant_id in variants:
            try:
                Variant.objects.get(id=variant_id, question__id=question)
            except Variant.DoesNotExist:
                raise serializers.ValidationError(
                    f"This {variant_id} id variant is not related to the current {question} question."
                )
        return obj

    def validate_selected_variant(self, value):
        question_id = self.initial_data.get("question")
        question = TestQuestion.objects.get(id=question_id)
        if question.type == "single_select" and len(value) > 1:
            raise serializers.ValidationError(
                f"This '{question}' question is not in multi selected type"
            )
        return value

    def validate_is_true(self, value):
        check = check_answers(
                self.initial_data.get("question"),
                self.initial_data.get("selected_variant"),
            )
        return check
