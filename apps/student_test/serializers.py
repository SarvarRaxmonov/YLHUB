from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from apps.student_test.models import Test, UserTest


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("id", "name", "time", "resumbit_attempt_count", "questions")


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ("test", "start_time", "end_time")

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return UserTest.objects.create(**validated_data)

    def validate(self, data):
        current_time = timezone.now().strftime("%Y-%m-%dT%H:%M")
        test = UserTest.objects.filter(user=self.context.get("request").user, end_time__gte=current_time)
        if test.exists():
            raise ValidationError("You can not do multiple tests at the same time please solve your current test")
        return data

    def validate_start_time(self, value):
        current_time = timezone.now()
        if value > current_time:
            raise ValidationError("Start time cannot be in the future.")
        return value

    def validate_end_time(self, value):
        test_taken = Test.objects.get(id=self.initial_data.get("test"))
        start_time = datetime.strptime(self.initial_data.get("start_time"), "%Y-%m-%dT%H:%M")
        end_time = datetime.strptime(self.initial_data.get("end_time"), "%Y-%m-%dT%H:%M")
        expected_end_time = start_time + test_taken.time
        if end_time != expected_end_time:
            raise ValidationError("Expected right calculated end time for user test.")
        return value
