from rest_framework import serializers

from .models import Announcement, Category, News, Poll, PollChoice, UserChoice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "category",
            "type",
            "created_at",
        )

    def get_type(self, obj):
        return obj.__class__.__name__


class NewsDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    type = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ("id", "title", "image", "category", "type", "created_at", "content")

    def get_type(self, obj):
        return obj.__class__.__name__


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = (
            "id",
            "title",
            "image",
            "location",
            "date",
            "type",
            "content",
            "created_at",
        )

    def get_type(self, obj):
        return obj.__class__.__name__


class PollChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollChoice
        fields = ("id", "name")


class PollDetailSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    choices = PollChoiceSerializer(many=True)
    choice_count = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = (
            "id",
            "title",
            "image",
            "type",
            "choices",
            "created_at",
            "choice_count",
        )

    def get_type(self, obj):
        return obj.__class__.__name__

    def get_choice_count(self, obj):
        values = [_ for _ in obj.choices.all()]
        return UserChoice.objects.filter(choice__in=values).count()
