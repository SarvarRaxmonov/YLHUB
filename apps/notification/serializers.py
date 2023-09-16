from rest_framework import serializers

from apps.main.models import Announcement, News, Poll
from apps.notification.models import Notification, UserNotification


class PollSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ("id", "title", "image", "type", "created_at")

    def get_type(self, obj):
        return obj.__class__.__name__


class NewsSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ("id", "title", "image", "type", "created_at")

    def get_type(self, obj):
        return obj.__class__.__name__


class AnnouncementSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = ("id", "title", "image", "type", "created_at")

    def get_type(self, obj):
        return obj.__class__.__name__


class NotificationSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ("id", "title", "text", "object_id", "content_object")

    def get_content_object(self, obj):
        content_object = obj.content_object

        if content_object:
            if isinstance(content_object, Poll):
                serializer = PollSerializer(content_object)
                return serializer.data
            elif isinstance(content_object, News):
                serializer = NewsSerializer(content_object)
                return serializer.data
            elif isinstance(content_object, Announcement):
                serializer = AnnouncementSerializer(content_object)
                return serializer.data
        return None


class UserNotificationListSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()

    class Meta:
        model = UserNotification
        fields = (
            "id",
            "user",
            "notification",
            "is_read",
            "created_at",
        )
