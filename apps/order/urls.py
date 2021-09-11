from django.urls import path

from apps.order import views
from .views import CheckoutView, OrdersByUserView


urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('confirm_order/', CheckoutView.post, name='confirm-order'),
    path('orders_by_user/', OrdersByUserView.as_view(), name='orders_by_user')
]