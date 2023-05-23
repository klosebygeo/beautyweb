from django.db import models

from shop.models import Product


# Create your models here.


class Cart(models.Model):
    id_user = models.IntegerField(null=False)
    produs = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    status = models.BooleanField(null=False, default=0)
