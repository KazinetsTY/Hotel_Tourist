from django import forms

from hotel_room.models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

