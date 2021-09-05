from django.db import models

from apps.product.models import Product
from apps.user.models import MyUser


class ProductCart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'ProductCart no. {self.id}'


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductCart)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

    def __str__(self):
        return f'Cart no. {self.id}'