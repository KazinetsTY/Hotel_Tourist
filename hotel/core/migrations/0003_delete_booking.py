# Generated by Django 4.2 on 2023-04-25 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]