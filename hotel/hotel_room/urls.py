from django.urls import path

from hotel_room.views import index

app_name = "hotel_room"


urlpatterns = [
    path("", index, name="list"),
]
