from django.db import models
from employees.models import Employee
from datetime import datetime


class Custody(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.description
