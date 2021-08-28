from django.db import models

from apps.product.models import Product
from apps.user.models import MyUser


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart no. {self.id}'


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'ProductCart no. {self.id}'
