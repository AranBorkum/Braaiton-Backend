# Generated by Django 5.0 on 2023-12-14 13:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookingModel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("item_id", models.UUIDField()),
                ("customer", models.JSONField(null=True)),
                ("duration", models.IntegerField(default=2)),
                ("start_time", models.DateTimeField(null=True)),
                ("stage", models.IntegerField(default=1)),
            ],
        ),
    ]