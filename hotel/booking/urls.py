from django.urls import path

from booking import views

app_name = "booking"

urlpatterns = [
    path("", views.BookingListView.as_view(), name="list"),
    path("<int:room_id>/create/", views.BookingCreateView.as_view(), name="create"),
]
