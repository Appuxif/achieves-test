from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Note(models.Model):
    """Note"""

    title = models.CharField(
        verbose_name="Title",
        max_length=128,
        db_index=True,
    )
    body = models.TextField(
        verbose_name="Body",
    )
    user = models.ForeignKey(
        User,
        verbose_name="User",
        on_delete=models.CASCADE,
        db_index=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        db_index=True,
        auto_now_add=True,
    )
