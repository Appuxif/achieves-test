from uuid import uuid4

from django.utils import timezone


def file_upload_to(instance, filename):
    now = timezone.now()
    uuid = uuid4().hex
    name = instance.__class__.__name__.lower()
    file_ext = filename.split(".")[-1]
    return f"{name}/{now.year}/{now.month}/{now.day}/{instance.id}{uuid}.{file_ext}"
