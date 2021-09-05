from django.urls import path
from apps.order import views
from .views import CheckoutView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('confirm_order', views.confirm_order, name='confirm_order'),
]