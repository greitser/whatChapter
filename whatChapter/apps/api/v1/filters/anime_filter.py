from django_filters.rest_framework import FilterSet

from whatChapter.apps.whatChapter.models import Anime


class AnimeFilterSet(FilterSet):
    class Meta:
        model = Anime
        fields = ["anime_name", "genres", "rating", "studio"]
