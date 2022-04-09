from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from whatChapter.apps.api.v1 import serializers, filters
from whatChapter.apps.api.v1.permissions import IsOwner
from whatChapter.apps.api.v1.filters.user_filter import UserFilterSet
from whatChapter.apps.whatChapter.models import User


@extend_schema(tags=["User"])
class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    authentication_classes = (JWTAuthentication,)
    authentication_action_classes = {"create": tuple()}
    serializer_class = serializers.UserSerializer
    serializer_action_classes = {"create": serializers.UserCreateSerializer}
    permission_classes = (IsOwner,)
    permission_action_classes = {
        "create": (permissions.AllowAny,),
        "list": (permissions.IsAdminUser,),
    }

    pagination_class = LimitOffsetPagination
    filterset_class = filters.UserFilterSet
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-date_joined",)

    INVALID_PASSWORD_DATA = {
        "message": "Password does not match",
        "code": "invalid_user_password",
    }

    def get_queryset(self) -> QuerySet:
        return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_authenticators(self):
        try:
            return self.authentication_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_authenticators()

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_action_classes[self.action]
            ]
        except (KeyError, AttributeError):
            return super().get_permissions()

    @action(
        detail=False, pagination_class=None, filterset_class=None, filter_backends=None
    )
    def me(self, _: Request) -> Response:
        serializer = serializers.UserSerializer(
            self.request.user, context=self.get_serializer_context()
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)
