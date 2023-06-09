from django.db import models

from employee.models import Employee


# Create your models here.
class Service(models.Model):

    name_of_service = models.TextField(max_length=300)
    price = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_of_service


STATUS = (
    ('draft', 'draft'),
    ('completed', 'completed')
)

# model de servicii rezervate in models.py - fields:  id_serviciu, id_user, status(choices: draft, completed),
# angajat_id, data(de tip datetime)
class RezervareServicii(models.Model):
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    id_user = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=9, default='draft')
    id_angajat = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True)



from django.contrib.auth.models import User

class Programare(models.Model):
    angajat = models.ForeignKey(User, on_delete=models.CASCADE)
    data_ora = models.DateTimeField()

    def __str__(self):
        return f"Programare cu {self.angajat.username} la {self.data_ora}"
