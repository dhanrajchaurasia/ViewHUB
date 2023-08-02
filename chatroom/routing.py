from . import consumer
from django.urls import path

websocket_urlpatterns = [
    path('ws/sc/',consumer.StreamConsumer.as_asgi()),
    path('ws/ac/',consumer.StreamConsumer.as_asgi()),

]