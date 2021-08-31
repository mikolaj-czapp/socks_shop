from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.cart.models import ProductCart
from apps.cart.models import Cart


class CartByUserView(LoginRequiredMixin, View):
    template_name ='shopping/cart.html'

    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(user=self.request.user)
            context = {
                'object': cart
            }
            return render(self.request, 'shopping/cart.html', context)
        except ObjectDoesNotExist:
            return redirect("/")