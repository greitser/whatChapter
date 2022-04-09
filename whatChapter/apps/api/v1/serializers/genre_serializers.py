from rest_framework import serializers

from whatChapter.apps.whatChapter.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GenreIdNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "genre_name"]
