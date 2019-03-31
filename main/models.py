from django.db import models


class Task(models.Model):
    PRIORITIES = ((0, "low"),
                  (1, "normal"),
                  (2, "high"),
                  (3, "critical"))
    # the id field is created automatically
    name = models.CharField(max_length=600)
    priority = models.IntegerField(choices=PRIORITIES, default=1)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)  # new ones first
