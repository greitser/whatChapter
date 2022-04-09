from django_filters.rest_framework import FilterSet, filters

from whatChapter.apps.whatChapter.models import User


class UserFilterSet(FilterSet):

    username = filters.CharFilter(lookup_expr="icontains")
    email = filters.CharFilter(lookup_expr="icontains")
    first_name = filters.CharFilter(lookup_expr="icontains")
    last_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["username", "id", "email", "first_name", "last_name"]
