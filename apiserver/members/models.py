import uuid

from django.db import models


class Member(models.Model):
    GENDER_CHOICES = (
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("NB", "NB"),
        ("Không tiết lộ", "Không tiết lộ"),
    )

    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["id"]
