from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.checks import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy


from hotel_room import models
from hotel_room.mixins import FormRequestKwargMixin

from hotel_room import forms


class IndexView(TemplateView):
    template_name = "base.html"


class RoomListView(ListView):
    permission_required = "hotel_room.view_room"
    context_object_name = "room"
    template_name = "hotel_room/list.html"
    model = models.Room


class RoomCreateView(PermissionRequiredMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    permission_required = "hotel_room.add_room"
    form_class = forms.RoomForm
    template_name = "hotel_room/create.html"
    success_url = reverse_lazy('hotel_room:list')
    success_message = "Запись успешно создана"


class RoomDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "hotel_room.view_room"
    model = models.Room
    template_name = "hotel_room/detail.html"
    context_object_name = "room"


class RoomUpdateView(FormRequestKwargMixin,
                     PermissionRequiredMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    permission_required = "hotel_room.change_room"
    model = models.Room
    context_object_name = "room"
    template_name = "hotel_room/update.html"
    form_class = forms.RoomForm
    success_message = "Запись успешно обновлена"

