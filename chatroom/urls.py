from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:room_name>/<str:created>', views.stream, name="stream"),
    # path('<str:room_name>', views.stream, name="stream"),
]