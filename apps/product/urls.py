from django.urls import path

from apps.product import views
from apps.product.views import ProductListView, add_to_cart, remove_from_cart

urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),
]