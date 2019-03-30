from django.db import models


class Task(models.Model):
    priorities = ((0, "low"),
                  (1, "normal"),
                  (2, "high"),
                  (3, "critical"))

    name = models.CharField(max_length=300)
    priority = models.IntegerField(choices=priorities)
    date_created = models.DateField(auto_now_add=True)

