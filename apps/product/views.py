from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

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
    product_cart = ProductCart.objects.create(product=item, user=request.user)
    cart = Cart.objects.filter(user=request.user)
    if cart.exists():
        cart = cart[0]
        # check if product is in the cart
        if cart.items.filter(product__id=item.id).exists():
            product_cart.quantity += 1
            product_cart.save()
        else:
            cart = Cart.objects.create(user=request.user)
            cart.items.add(product_cart)
    return redirect('product_detail', pk=slug)
