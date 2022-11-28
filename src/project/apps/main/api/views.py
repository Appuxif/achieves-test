import math

import django_filters.rest_framework
from django.utils import timezone
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from project.apps.adverts.models import Advert
from project.apps.events.models import Event
from project.apps.main.api.serializers import FeedWithAdvertSerializer


class AdvertPagination(LimitOffsetPagination):
    """
    Пагинация с рекламой.

    Добавляет к списку элементов рекламные записи через каждые два элемента, если
    в БД имеются опубликованные рекламные записи.
    Количество рекламных записей, который запрашиваются из БД, рассчитывается на основе
    запрошенного количества элементов.
    """

    adverts_objects = None

    def get_limit(self, request):
        limit = super().get_limit(request)

        self.adverts_objects = Advert.objects.none()
        adverts_count = math.ceil(limit / 3)
        if adverts_count:
            now = timezone.now()
            self.adverts_objects = Advert.objects.filter(published_at__lt=now)
            self.adverts_objects = self.adverts_objects.order_by("-published_at")
            self.adverts_objects = self.adverts_objects[:adverts_count]

        return limit

    def paginate_queryset(self, queryset, request, view=None):
        page = super().paginate_queryset(queryset, request, view)
        if page:
            page = self.enrich_page_with_adverts(page)
        return page

    def enrich_page_with_adverts(self, page):
        """Добавляет рекламные записи в список через каждые два элемента"""

        adverts = iter(self.adverts_objects)
        page = iter(page)

        def generate_items():
            while True:
                item = next(page, None)
                if item is None:
                    return
                yield item
                yield next(page, None)
                yield next(adverts, None)

        return list(item for item in generate_items() if item is not None)


class FeedFilterSet(django_filters.FilterSet):
    user_id = django_filters.NumberFilter()

    class Meta:
        model = Event
        fields = ("user_id", "content_type")


class FeedAPIView(ListAPIView):
    """Feed"""

    serializer_class = FeedWithAdvertSerializer
    queryset = Event.objects.all().order_by("-created_at")
    pagination_class = AdvertPagination
    filter_backends = [
        filters.SearchFilter,
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    filterset_class = FeedFilterSet
    search_fields = [
        "user_achieves__achieve__title",
        "notes__title",
    ]
