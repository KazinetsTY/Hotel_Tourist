from django import forms

from booking.models import Booking
from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput


class BookRoom(forms.ModelForm):
    start_date = forms.DateField(
        label="Дата заезда",
        required=True,
        widget=DatePickerInput(
            options=FlatpickrOptions(altFormat="d.m.Y")
        )
    )
    end_date = forms.DateField(
        label="Дата выезда",
        required=True,
        widget=DatePickerInput(
            options=FlatpickrOptions(altFormat="d.m.Y")
        )
    )

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.room_id = self.request.room_id
        instance.save()
        instance.user = self.request.user
        instance.save()
        return instance

    class Meta:
        model = Booking
        fields = (
            "start_date",
            "end_date",
            "comment"
        )
