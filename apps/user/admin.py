from django.contrib import admin

from apps.user.models import ProductCart, Cart, Order, MyUser

admin.site.register(ProductCart)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(MyUser)
