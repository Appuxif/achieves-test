from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User"""

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
