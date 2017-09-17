from django.db import models
from .pak import Pak

class Family(models.Model):
    name = models.CharField(null=False, max_length=256)

    FAMILY_TYPE = (
        (0, "FIRST RESPONDER"),
        (1, "VOLUNTEER"),
        (2, "USER")
    )

    family_type = models.IntegerField(choices = FAMILY_TYPE)

    pak = models.ForeignKey(
        Pak,
        on_delete=models.CASCADE,
        related_name="families",
        null=False)
