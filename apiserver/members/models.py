from django.db import models


# Create your models here.
class Member(models.Model):
    GENDER_CHOICES = (
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("NB", "NB"),
        ("Không tiết lộ", "Không tiết lộ"),
    )

    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    institution = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
