from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View

from .forms import OrderForm

from .models import Order
from ..cart.models import Cart
from django.contrib import messages

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=self.request.user)
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
        if form.is_valid():
            return redirect('home')
