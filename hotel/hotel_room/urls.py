from django.urls import path

from hotel_room import views

app_name = "hotel_room"


urlpatterns = [
    path("", views.RoomListView.as_view(), name="list"),
    path("create/", views.RoomCreateView.as_view(), name="create"),
    path("<int:pk>/", views.RoomDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.RoomUpdateView.as_view(), name="update"),
]
