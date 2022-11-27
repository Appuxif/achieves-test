from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.apps.achieves.models import UserAchieve
from project.apps.events.models import Event
from project.apps.notes.models import Note


@receiver(post_save, sender=UserAchieve)
@receiver(post_save, sender=Note)
def create_achieve_event(instance, created, **kwargs):
    if created:
        Event.objects.create(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            user=instance.user,
        )
