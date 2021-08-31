from django.urls import path
from apps.cart import views


urlpatterns = [
    path('cart/', views.CartByUserView.as_view(), name='cart_by_user'),
]