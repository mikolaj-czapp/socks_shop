from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.list import ListView
from django.views.generic import DetailView
from apps.product.models import Product
from apps.cart.models import Cart, ProductCart


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


@login_required
def add_to_cart(request, **kwargs):
    slug = 0
    for kw in kwargs:
        slug = kwargs[kw]
    item = get_object_or_404(Product, id=slug)
    product_cart, created = ProductCart.objects.get_or_create(product=item, user=request.user)
    cart = Cart.objects.filter(user=request.user)
    if cart.exists():
        cart = cart[0]
        # check if product is in the cart
        if cart.items.filter(product__id=item.id).exists():
            product_cart.quantity += 1
            product_cart.save()
            messages.info(request, "Zaktualizowano ilość produktu w koszyku.")
            return redirect('product_detail', pk=slug)
        else:
            cart.items.add(product_cart)
            messages.info(request, "Dodano do koszyka.")
            return redirect('product_detail', pk=slug)
    else:
        cart = Cart.objects.create(user=request.user)
        cart.items.add(product_cart)
        messages.info(request, "Dodano do koszyka.")
        return redirect('product_detail', pk=slug)
