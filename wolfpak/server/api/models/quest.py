from django.db import models

class Quest(models.Model):
    created_on = models.DateTimeField(null = False)
    completed_on = models.DateTimeField(null = False)

    x_coord = models.FloatField()
    y_coord = models.FloatField()

    # actual emojis
    message = models.CharField(null = False, max_length=256)

    owner = models.ForeignKey(
        "Wolf",
        on_delete=models.CASCADE,
        related_name="owner",
        null=False)

'''
    assignee = models.ForeignKey(
        "Wolf",
        on_delete=models.CASCADE,
        related_name="assignee")
'''
