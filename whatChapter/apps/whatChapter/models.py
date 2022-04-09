import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# from whatChapter.apps.api.v1.managers import UserManager


class User(AbstractUser):
    id = models.UUIDField(
        unique=True, primary_key=True, editable=False, default=uuid.uuid4
    )
    rating = models.FloatField(default=0.0)
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Genre(models.Model):
    id = models.UUIDField(
        unique=True, primary_key=True, editable=False, default=uuid.uuid4
    )
    genre_name = models.TextField()
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    approved = models.BooleanField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)


class Studio(models.Model):
    id = models.UUIDField(
        unique=True, primary_key=True, editable=False, default=uuid.uuid4
    )
    name = models.TextField()
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    image = models.ImageField(null=True)
    approved = models.BooleanField(default=False)


class Anime(models.Model):
    STATUS_FINISH = "status_finish"
    STATUS_WAIT = "status_wait"
    STATUS_ISSUED = "status_issued"

    STATUSES = (
        (STATUS_FINISH, "status_finish"),
        (STATUS_WAIT, "status_wait"),
        (STATUS_ISSUED, "status_wait"),

    )
    id = models.UUIDField(
        unique=True, primary_key=True, editable=False, default=uuid.uuid4
    )
    anime_name = models.CharField(max_length=255)
    number_episodes = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre)
    year_issue = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    studio = models.ManyToManyField(Studio)
    image = models.ImageField(null=True)
    approved = models.BooleanField(default=False)
    chapter = models.IntegerField(null=True)
    status = models.CharField(choices=STATUSES, max_length=15, default=STATUS_WAIT)

    class Meta:
        indexes = [GinIndex(fields=["anime_name"])]
