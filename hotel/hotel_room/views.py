from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from hotel_room.models import Room


def index(request: HttpRequest) -> HttpResponse:
    qs = Room.objects.all()
    return render(request, "hotel_room/list.html", {"room": qs})
