from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/user/(?P<username>\w+)/?$", consumers.StatsStreamConsumer.as_asgi()),
]
