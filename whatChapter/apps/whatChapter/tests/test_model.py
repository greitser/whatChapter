import pytest

# Create your tests here.
from mixer.backend.django import mixer

from whatChapter.apps.whatChapter.models import User


@pytest.mark.django_db
class TestModels:
    def test_str_user(self, caplog):
        user = mixer.blend(User)
        assert user.email == str(user)
