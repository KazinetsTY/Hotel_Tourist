from django import forms
from hotel_room import models

from hotel_room.models import Room, Booking


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

# TODO добавить виджеты
class BookRoom(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

