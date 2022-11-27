from django.db import models

from project.core.utils.models import file_upload_to


class Advert(models.Model):
    """Advert"""

    title = models.CharField(
        verbose_name="Title",
        max_length=128,
        db_index=True,
    )
    description = models.TextField(
        verbose_name="Description",
    )
    image = models.ImageField(
        verbose_name="Image",
        upload_to=file_upload_to,
    )
    url = models.URLField(verbose_name="URL", max_length=256)
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        db_index=True,
    )
    published_at = models.DateTimeField(
        verbose_name="Published At",
        db_index=True,
    )
