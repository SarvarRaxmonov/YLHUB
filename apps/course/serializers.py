from datetime import datetime, timedelta

from rest_framework import serializers

from apps.course.models import Course, Language, Lesson, LessonProgress


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ("id", "name")


class CourseListSerializer(serializers.ModelSerializer):
    language = LanguageSerializer()
    data = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "score",
            "language",
            "type",
            "image",
            "data",
        )

    def get_data(self, obj):
        all_lessons = obj.lessons.all()
        count = LessonProgress.objects.filter(user=self.context["request"].user, is_completed=True).count()
        if count:
            data = {"percentage": round(count / all_lessons.count() * 100)}
            return data
        # else:
        #     data = {
        #         "is_finished": True
        #     }
        #     return data
        return datetime.now().date() + timedelta(days=obj.duration_days)


class CourseLessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "title", "type", "order")


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson_list = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "title", "desc", "type", "language", "lesson_count", "duration_days", "score", "lesson_list", "data")

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_lesson_list(self, obj):
        lessons = obj.lessons.all()
        lesson_serializer = CourseLessonListSerializer(lessons, many=True)
        return lesson_serializer.data

    def get_data(self, obj):
        all_lessons = obj.lessons.all()
        count = LessonProgress.objects.filter(user=self.context["request"].user, is_completed=True).count()
        if count:
            data = {"percentage": round(count / all_lessons.count() * 100)}
            return data
