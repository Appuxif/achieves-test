from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from project.apps.events.models import Event
from project.core.utils.models import file_upload_to

User = get_user_model()


class Achieve(models.Model):
    """Achieve"""

    title = models.CharField(
        verbose_name="Title",
        max_length=128,
        db_index=True,
    )
    description = models.TextField(
        verbose_name="Description",
    )
    icon = models.ImageField(
        verbose_name="Icon",
        upload_to=file_upload_to,
    )


class UserAchieve(models.Model):
    """User Achieve"""

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    achieve = models.ForeignKey(
        Achieve, verbose_name="Achieve", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name="Created At", auto_now_add=True, db_index=True
    )
    events = GenericRelation(
        Event,
        related_query_name="user_achieves",
    )
