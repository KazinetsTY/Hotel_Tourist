from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView
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


# TODO success_message доработать вывод на экран
class RoomCreateView(PermissionRequiredMixin,
                     LoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    permission_required = "hotel_room.view_room"
    form_class = forms.RoomForm
    template_name = "hotel_room/create.html"
    success_url = reverse_lazy('hotel_room:list')
    success_message = "Запись успешно создана"


# TODO разобраться почему не выводятся детали номера
class RoomDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "hotel_room.view_room"
    model = models.Room
    template_name = "hotel_room/detail.html"
    context_object_name = "detail"


# TODO добавить в html-файл редактировать номер
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


# TODO переделать booking
def book_room(request, pk):
    form = forms.BookRoom
    return render(request, 'hotel_room/booking/booking.html', {'form': form})
