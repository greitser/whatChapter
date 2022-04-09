from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from whatChapter.apps.api.v1 import views

router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")
router.register("genre", views.GenreViewSet, basename="genre")
router.register("studio", views.StudioViewSet, basename="studio")
router.register("anime", views.AnimeViewSet, basename="anime")
urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("", include(router.urls)),
]
