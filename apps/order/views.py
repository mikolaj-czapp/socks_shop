from django.shortcuts import render, redirect
from django.views import View

from .forms import OrderForm

from .models import Order


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = OrderForm
        context = {
            'form': form
        }
        return render(self.request, 'shopping/order.html', context)

    def post(self, *args, **kwargs):
        form = OrderForm(self.request.POST or None)
        if form.is_valid():
            return redirect('checkout')
