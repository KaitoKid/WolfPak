from django.db import models

class Pak(models.Model):
    name = models.CharField(null=False, max_length=256)
    location = models.CharField(null=False, max_length=256)
