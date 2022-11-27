from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from project.apps.achieves.models import Achieve, UserAchieve
from project.apps.adverts.models import Advert
from project.apps.events.models import Event
from project.apps.notes.models import Note
from project.apps.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """User Admin"""


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Note Admin"""

    list_display = ("pk", "title", "created_at")
    raw_id_fields = ("user",)


@admin.register(Achieve)
class AchieveAdmin(admin.ModelAdmin):
    """Achieve Admin"""

    list_display = ("pk", "title")


@admin.register(UserAchieve)
class UserAchieveAdmin(admin.ModelAdmin):
    """User Achieve Admin"""

    list_display = ("pk", "created_at")
    raw_id_fields = ("achieve", "user")


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Advert Admin"""

    list_display = ("pk", "title", "created_at", "published_at")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Event Admin"""

    list_display = ("pk", "content_type", "object_id", "created_at")
    raw_id_fields = ("content_type",)
