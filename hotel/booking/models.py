from django.db import models

from core.models import User
from hotel_room.models import Room


class Booking(models.Model):
    start_date = models.DateField(auto_now_add=False, verbose_name="Дата заезда", blank=False)
    end_date = models.DateField(auto_now_add=False, verbose_name="Дата выезда", blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Гость", blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField(verbose_name="Пожелания", blank=True)

    def __str__(self):
        return self.room

    def get_absolute_url(self):
        return f'/booking/{self.pk}'

    class Meta:
        verbose_name = "Забронированый номер"
        verbose_name_plural = "Забронированые номера"
        ordering = ["-start_date"]
        get_latest_by = "created_at"
