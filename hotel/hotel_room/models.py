from django.db import models
from django.urls import reverse_lazy


class Room(models.Model):
    class TypeChoices(models.TextChoices):
        SINGLE = "Одноместный стандарт"
        SINGLE_COMFORT = "Одноместный комфорт"
        SINGLE_COMFORT_PLUS = "Одноместный комфорт пдюс"
        TWIN = "Двухместный стандарт"
        TWIN_COMFORT = "Двухместный комфорт"
        DOUBLE = "Двухместный комфорт плюс"
        LUX = "Люкс"
        __empty__ = "Выберите тип номера"

    type = models.CharField(max_length=50, choices=TypeChoices.choices, blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name="Название номера")
    description = models.TextField(blank=True, verbose_name="Описание номера")
    price = models.CharField(max_length=15, verbose_name="Стоимость номера в сутки")

    def get_absolute_url(self):
        return reverse_lazy("hotel_room:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"
        ordering = ['price']
