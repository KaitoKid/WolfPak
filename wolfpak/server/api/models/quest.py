from django.db import models

class Quest(models.Model):
    STATUS = (
        (0, "AVAILABLE"),
        (1, "CLAIMED"),
        (2, "COMPLETED")
    )

    # request feed
    name = models.CharField(max_length=256)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(null=True)

    # request detail
    x_coord = models.FloatField(default=0.0)
    y_coord = models.FloatField(default=0.0)

    # actual emojis
    message = models.CharField(null = False, max_length=256)


'''
    owner = models.ForeignKey(
        "Wolf",
        on_delete=models.CASCADE,
        related_name="quests",
        null=False)


    assignee = models.ForeignKey(
        "Wolf",
        on_delete=models.CASCADE,
        related_name="assignee")
'''
