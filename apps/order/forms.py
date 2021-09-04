from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from apps.cart.models import Cart
from apps.order.models import Order


class OrderForm(forms.Form):
    shipping_address = forms.CharField()
    same_shipping_address = forms.BooleanField(widget=forms.CheckboxInput)