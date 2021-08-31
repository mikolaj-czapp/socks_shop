from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.brand} - {self.name}"

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={
            'slug': self.id
        })
