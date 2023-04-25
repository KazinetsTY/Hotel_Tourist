from django import forms
from hotel_room import models

from hotel_room.models import Room, Booking


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'


class BookingForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    room = forms.ModelChoiceField(queryset=Room.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'room']
