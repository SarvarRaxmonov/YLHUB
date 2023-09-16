from rest_framework import serializers

from apps.vebinar.models import Chat, Complain, UserSearchVebinar, Vebinar


class VebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vebinar
        fields = (
            "name",
            "url",
            "speaker",
            "status",
            "thumbnail",
            "type",
            "description",
        )


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ("user", "vebinar", "type", "text")


class UserSearchVebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearchVebinar
        fields = ("user", "keyword")


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("user", "vebinar", "room", "content", "timestamp")
