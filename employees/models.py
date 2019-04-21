from django.db import models
from datetime import datetime


class Employee(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
