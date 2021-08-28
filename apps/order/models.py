from django.db import models

from apps.cart.models import Cart
from apps.user.models import MyUser


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.OneToOneField(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=70)
    ordered_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.id

