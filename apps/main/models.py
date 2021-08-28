from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    BRANDS = (
        ('SX', 'SOXO'),
        ('MAR', "MARLIN"),
        ('MM', 'MANY MORNINGS')
    )
    name = models.CharField(max_length=50)
    brand = models.CharField(choices=BRANDS, max_length=50)
    description = models.TextField(blank=True)
    category_id = models.ForeignKey(Category, default='Unbranded', on_delete=models.SET_DEFAULT)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.brand} - {self.name}"

