# Generated by Django 5.0 on 2023-12-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking_service", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingmodel",
            name="payment_id",
            field=models.UUIDField(null=True),
        ),
    ]
