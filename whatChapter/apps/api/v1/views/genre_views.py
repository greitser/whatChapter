
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from whatChapter.apps.api.v1 import filters, serializers
from whatChapter.apps.whatChapter.models import Genre


@extend_schema(tags=["Genre"])
class GenreViewSet(
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
    queryset = Genre.objects.filter(approved=True)
    pagination_class = LimitOffsetPagination
    filterset_class = filters.GenreFilterSet
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    serializer_class = serializers.GenreSerializer

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_action_classes[self.action]
            ]
        except (KeyError, AttributeError):
            return super().get_permissions()
