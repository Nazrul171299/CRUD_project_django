from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()
    price = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.name
