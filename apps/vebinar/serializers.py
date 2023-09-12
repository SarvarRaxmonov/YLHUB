from rest_framework import serializers

from apps.vebinar.models import Complain, UserSearchVebinar, Vebinar


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
