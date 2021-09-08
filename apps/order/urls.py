from django.urls import path
from .views import CheckoutView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('confirm_order/', CheckoutView.post, name='confirm-order')
]