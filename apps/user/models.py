from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=70)
    postal_code = models.CharField(max_length=6)

    def get_address(self):
        return f'{self.street} {self.postal_code} {self.city}'

    def __str__(self):
        return self.username



