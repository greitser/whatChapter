from rest_framework import serializers

from .genre_serializers import GenreIdNameSerializer
from whatChapter.apps.whatChapter.models import Anime, Genre


class AnimeGetSerializer(serializers.ModelSerializer):
    genres = GenreIdNameSerializer(many=True)

    class Meta:
        model = Anime
        fields = "__all__"


class AnimeCreateUpdateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Anime
        fields = "__all__"
