from django.contrib import admin

from apps.main.models import Category, Product, ProductCart, Cart, Order, MyUser

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductCart)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(MyUser)


