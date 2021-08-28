from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, default='No brand', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    category_id = models.ForeignKey(Category, default='No category', on_delete=models.SET_DEFAULT)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.brand} - {self.name}"
