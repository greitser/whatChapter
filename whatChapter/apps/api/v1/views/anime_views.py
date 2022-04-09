from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from whatChapter.apps.api.v1 import filters, serializers
from whatChapter.apps.whatChapter.models import Anime


@extend_schema(tags=["Anime"])
class AnimeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (permissions.IsAdminUser,)
    permission_action_classes = {
        "list": (permissions.AllowAny,),
        "retrieve": (permissions.AllowAny,),
    }
    queryset = Anime.objects.filter(approved=True)
    pagination_class = LimitOffsetPagination
    filterset_class = filters.AnimeFilterSet
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    serializer_class = serializers.AnimeCreateUpdateSerializer
    serializer_action_classes = {
        "list": serializers.AnimeGetSerializer,
        "retrieve": serializers.AnimeGetSerializer,
    }

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_action_classes[self.action]
            ]
        except (KeyError, AttributeError):
            return super().get_permissions()

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
