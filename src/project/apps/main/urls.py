from django.urls import path

from project.apps.main.api.views import FeedAPIView

app_name = "main"

urlpatterns = [
    path("api/feed/", FeedAPIView.as_view(), name="feed"),
]
