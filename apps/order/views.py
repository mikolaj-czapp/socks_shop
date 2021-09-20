from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View


from .forms import OrderForm

from .models import Order
from ..cart.models import Cart
from django.contrib import messages


class CheckoutView(LoginRequiredMixin, View):
    """
    A checkout view when user confirms his cart for ordering.
    """
    def get(self, *args, **kwargs):
        # Gets the most recent cart of the user and passes it to the checkout.
        try:
            user_carts = Cart.objects.filter(user=self.request.user).count()
            cart = Cart.objects.filter(user=self.request.user).all()[user_carts - 1]
            form = OrderForm
            context = {
                'form': form,
                'cart': cart
            }
            return render(self.request, 'shopping/checkout.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect('home')

    def post(self, *args, **kwargs):
        # Get the order information from the user via a form and create an Order object in the database.
        form = OrderForm(self.request.POST or None)
        user_carts = Cart.objects.filter(user=self.request.user).count()
        if form.is_valid():
            same_shipping_address = form.cleaned_data.get("same_shipping_address")
            if same_shipping_address:
                shipping_address = self.request.user.get_address()
            else:
                shipping_address = form.cleaned_data.get("shipping_address")
            order = Order(
                user=self.request.user,
                cart=Cart.objects.filter(user=self.request.user)[user_carts - 1],
                shipping_address=shipping_address,
                ordered_on=datetime.now(),
                status=True
            )
            order.save()
            Cart.objects.create(user=self.request.user)
            messages.success(self.request, "Order succesfuly submitted.")
            return redirect('home')
        else:
            messages.error(self.request, "Order form invalid. Try again or contact us.")
            return redirect('home')


class OrdersByUserView(LoginRequiredMixin, View):
    """
    For showing the orders of the user.
    """
    def get(self,  *args, **kwargs):
        try:
            orders = Order.objects.filter(user=self.request.user)
            context = {
                'object': orders
            }
            if not orders.exists():
                messages.info(self.request, "You do not have an active order.")
                return redirect('home')
            return render(self.request, 'shopping/orders_by_user.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order.")
            return redirect('home')
