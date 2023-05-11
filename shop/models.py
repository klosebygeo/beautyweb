
from django.db import models

PRODUCT_TYPES = [
    (1, 'Ingrijire par'),
    (2, 'Ingrijire barba'),
    (3, 'Accesorii'),
]

class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    description = models.CharField(max_length=150, null=False)
    image = models.ImageField(upload_to='uploads/')
    tip_produs = models.CharField(choices=PRODUCT_TYPES, max_length=20)

    def __str__(self):
        return self.name






