from django.db import models

# Create your models here.
class Wolf(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    family = models.ForeignKey(
        "Family",
        on_delete=models.CASCADE,
        related_name="wolf",
        null=False)
