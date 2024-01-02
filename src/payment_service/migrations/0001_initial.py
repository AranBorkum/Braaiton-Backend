# Generated by Django 5.0 on 2023-12-15 08:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PaymentModel",
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
                ("amount", models.IntegerField()),
                ("payment_intent_id", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
