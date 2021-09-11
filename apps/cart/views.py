from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.cart.models import Cart


class CartByUserView(LoginRequiredMixin, View):
    template_name = 'shopping/cart.html'

    def get(self, *args, **kwargs):
        try:
            user_carts = max(0, Cart.objects.filter(user=self.request.user).count() - 1)
            if not user_carts:
                cart = Cart.objects.get(user=self.request.user)
            else:
                cart = Cart.objects.filter(user=self.request.user).all()[user_carts]
            context = {
                'object': cart
            }
            if not cart.items.all().exists():
                return redirect('empty-cart')
            return render(self.request, 'shopping/cart.html', context)
        except ObjectDoesNotExist:
            return redirect('empty-cart')


def empty_cart(request):
    return render(request, 'shopping/empty_cart.html')
