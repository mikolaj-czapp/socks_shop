from django.urls import path

from apps.product import views
from apps.product.views import ProductListView

urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
]
