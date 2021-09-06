from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView

from .forms import OrderForm

from .models import Order
from ..cart.models import Cart
from django.contrib import messages


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            user_carts = Cart.objects.filter(user=self.request.user).count() - 1
            cart = Cart.objects.filter(user=self.request.user).all()[user_carts]
            form = OrderForm
            context = {
                'form': form,
                'cart': cart
            }
            return render(self.request, 'shopping/order.html', context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect('home')

    def post(self, *args, **kwargs):
        form = OrderForm(self.request.POST or None)
        user_carts = Cart.objects.filter(user=self.request.user).count() - 1
        if form.is_valid():
            same_shipping_address = form.cleaned_data.get("same_shipping_address")
            if same_shipping_address:
                shipping_address = self.request.user.get_address()
            else:
                shipping_address = form.cleaned_data.get("shipping_address")
            order = Order(
                user=self.request.user,
                cart=Cart.objects.filter(user=self.request.user)[user_carts],
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
