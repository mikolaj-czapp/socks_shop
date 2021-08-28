from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.main.models import Product


class MyUser(AbstractUser):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=70)
    postal_code = models.CharField(max_length=6)

    def __str__(self):
        return self.username


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class ProductCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.id


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.OneToOneField(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=70)
    ordered_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.id



