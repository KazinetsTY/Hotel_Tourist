from django.db import models


class Room(models.Model):
    class TypeChoices(models.TextChoices):
        SINGLE = "single", "Одноместный стандарт"
        SINGLE_COMFORT = "single_comfort", "Одноместный комфорт"
        SINGLE_COMFORT_PLUS = "single_comfort_plus", "Одноместный комфорт пдюс"
        TWIN = "twin", "Двухместный стандарт"
        TWIN_COMFORT = "twin_comfort", "Двухместный комфорт"
        DOUBLE = "double", "Двухместный комфорт плюс"
        LUX = "triple", "Люкс"
        __empty__ = "Выберите тип номера"

    type = models.CharField(max_length=20, choices=TypeChoices.choices, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name="Название номера")
    description = models.TextField(blank=True, verbose_name="Описание номера")
    price = models.CharField(max_length=15, verbose_name="Стоимость номера в сутки")

    def __str__(self):
        return self.name

    def full_info(self):
        return f"Номер: {self.name}"

    full_info.short_description = "Подробнее..."

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"
        ordering = ['name']

