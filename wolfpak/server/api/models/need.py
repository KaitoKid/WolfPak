from django.db import models
from .quest import Quest

class Need(models.Model):
    NEEDS_TYPE = (
        (0, "911"),
        (1, "FIRSTAID"),
        (2, "EVACUATION"),
        (3, "WATER"),
        (4, "FOOD"),
        (5, "PHONECHARGE"),
        (6, "LIGHTS"),
        (7, "MEDICATION"),
        (8, "CLOTHING")
    )

    need = models.IntegerField(choices=NEEDS_TYPE)

    owner = models.ForeignKey(
        Quest,
        on_delete=models.CASCADE,
        related_name="needs",
        null=False)