from django.db import models


class Task(models.Model):
    PRIORITIES = ((0, "low"),
                  (1, "normal"),
                  (2, "high"),
                  (3, "critical"))
    # the id field is created automatically
    name = models.CharField(max_length=100, verbose_name="Description")
    priority = models.IntegerField(choices=PRIORITIES, default=1, verbose_name="Priority")
    date_created = models.DateField(auto_now_add=True, verbose_name="Date added")

    @property
    def fields_verbose(self):
        return dict([(f.name, f.verbose_name) for f in self._meta.fields + self._meta.many_to_many])

    class Meta:
        ordering = ('-id',)  # new ones first
