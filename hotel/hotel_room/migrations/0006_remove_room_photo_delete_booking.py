# Generated by Django 4.2 on 2023-04-29 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_room', '0005_rename_created_on_booking_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
