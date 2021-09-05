from django.contrib import admin

from apps.product.models import Category, Product, Brand


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "brand", "category", "price",)


# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)



