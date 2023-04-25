from django import forms
from hotel_room import models


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'
