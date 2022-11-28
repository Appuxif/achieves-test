from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from project.apps.achieves.models import UserAchieve
from project.apps.adverts.models import Advert
from project.apps.events.models import Event
from project.apps.notes.models import Note


class FeedSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, obj: Event):
        if isinstance(obj.content_object, UserAchieve):
            return (
                f"Пользователь {obj.content_object.user.first_name} "
                f"получил достижение {obj.content_object.achieve.title}"
            )
        if isinstance(obj.content_object, Note):
            return (
                f"Пользователь {obj.content_object.user.first_name} "
                f"написал заметку {obj.content_object.title}"
            )
        raise NotImplementedError

    class Meta:
        model = Event
        fields = ("id", "content_type", "object_id", "description", "created_at")


class AdvertSerializer(serializers.ModelSerializer):
    content_type = serializers.SerializerMethodField()
    object_id = serializers.IntegerField(source="id")

    def get_content_type(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        if content_type:
            return content_type.id
        return None

    class Meta:
        model = Advert
        fields = (
            "content_type",
            "object_id",
            "title",
            "description",
            "url",
            "created_at",
            "image",
        )


class FeedWithAdvertSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if isinstance(instance, Event):
            return FeedSerializer().to_representation(instance)
        if isinstance(instance, Advert):
            return AdvertSerializer().to_representation(instance)
        raise NotImplementedError
