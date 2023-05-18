from django.db import models


# Create your models here.


class Cart(models.Model):
    id_user = models.IntegerField(null=False)
    id_produs = models.IntegerField(null=False)
    status = models.BooleanField(null=False, default=0)
