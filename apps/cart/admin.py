from django.contrib import admin

from apps.cart.models import Cart, ProductCart

admin.site.register(Cart)
admin.site.register(ProductCart)
