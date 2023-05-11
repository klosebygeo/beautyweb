from django.db import models

from employee.models import Employee


# Create your models here.
class Service(models.Model):

    name_of_service = models.TextField(max_length=300)
    price = models.IntegerField()
    employee = models.CharField(max_length=30)

    def __str__(self):
        return self.name_of_service

