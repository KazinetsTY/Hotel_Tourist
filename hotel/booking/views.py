from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

from booking import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from booking import models

from hotel_room.mixins import FormRequestKwargMixin


class BookingListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "booking.view_book"
    context_object_name = "booking"
    template_name = "booking/list.html"
    model = models.Booking


class BookingCreateView(FormRequestKwargMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.BookRoom
    template_name = "booking/create.html"
    success_url = reverse_lazy("room:list")
    success_message = "Вы забронировали номер"
