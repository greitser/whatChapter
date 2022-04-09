
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from whatChapter.apps.api.v1 import filters, serializers
from whatChapter.apps.whatChapter.models import Studio


@extend_schema(tags=["Studios"])
class StudioViewSet(
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
    serializer_class = serializers.StudioSerializer
    queryset = Studio.objects.filter(approved=True)
    pagination_class = LimitOffsetPagination
    filterset_class = filters.StudioFilterSet
    filter_backends = (OrderingFilter, DjangoFilterBackend)

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_action_classes[self.action]
            ]
        except (KeyError, AttributeError):
            return super().get_permissions()
