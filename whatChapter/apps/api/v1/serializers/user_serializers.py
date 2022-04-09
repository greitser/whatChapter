from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from whatChapter.apps.whatChapter.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name")


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password", "username", "first_name", "last_name")

    def validate_password(self, value: str) -> str:
        return make_password(value)
