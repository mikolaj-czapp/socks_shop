from django.db import models
from django.contrib.auth.models import User
from apps.main.models import Product


class MyUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=70)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class ProductCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    ordered_on = models.DateTimeField()
    ordered = models.BooleanField(default=False)



