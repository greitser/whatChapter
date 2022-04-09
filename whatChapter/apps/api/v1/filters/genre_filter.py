from django_filters.rest_framework import FilterSet

from whatChapter.apps.whatChapter.models import Genre


class GenreFilterSet(FilterSet):
    class Meta:
        model = Genre
        fields = [
            "genre_name",
            "rating",
        ]
