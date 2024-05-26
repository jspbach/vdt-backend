# Generated by Django 5.0.6 on 2024-05-26 15:25

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unique_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("full_name", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Nam", "Nam"),
                            ("Nữ", "Nữ"),
                            ("NB", "NB"),
                            ("Không tiết lộ", "Không tiết lộ"),
                        ],
                        max_length=15,
                    ),
                ),
                ("institution", models.CharField(max_length=255)),
            ],
        ),
    ]