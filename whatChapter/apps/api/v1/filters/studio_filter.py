from django_filters.rest_framework import FilterSet

from whatChapter.apps.whatChapter.models import Studio


class StudioFilterSet(FilterSet):
    class Meta:
        model = Studio
        fields = [
            "name",
            "rating",
        ]
