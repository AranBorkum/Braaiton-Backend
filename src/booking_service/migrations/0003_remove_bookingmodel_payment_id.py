# Generated by Django 5.0 on 2023-12-15 11:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking_service", "0002_bookingmodel_payment_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookingmodel",
            name="payment_id",
        ),
    ]
