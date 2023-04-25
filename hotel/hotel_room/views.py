
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib import messages

from hotel_room import models
from hotel_room import const as room_const
from hotel_room.mixins import FormRequestKwargMixin

from hotel_room import forms


class RoomListView(ListView):
    permission_required = "hotel_room.view_room"
    context_object_name = "room"
    template_name = "hotel_room/list.html"
    queryset = models.Room.objects.all()


class RoomCreateView(PermissionRequiredMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    permission_required = "hotel_room.view_room"
    form_class = forms.RoomForm
    template_name = "hotel_room/create.html"
    success_url = reverse_lazy('hotel_room:list')
    success_message = "Запись успешно создана"


class RoomDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "hotel_room.view_room"
    model = models.Room
    template_name = "hotel_room/detail.html"
    context_object_name = "detail"


class RoomUpdateView(FormRequestKwargMixin,
                     PermissionRequiredMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    permission_required = "hotel_room.change_room"
    model = models.Room
    template_name = "hotel_room/update.html"
    form_class = forms.RoomForm
    success_message = "Запись успешно обновлена"


class RoomDeleteView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = "hotel_room.delete_room"
    model = models.Room
    success_url = reverse_lazy('hotel_room:list')
    success_message = "Запись успешно удалена"

    def get(self, *args, **kwargs):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return self.delete(*args, **kwargs)
