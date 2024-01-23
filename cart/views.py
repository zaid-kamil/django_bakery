from django.shortcuts import render, redirect, HttpResponse
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.models import Product

@login_required
def add_product_to_cart(request, pid):
    product = Product.objects.get(id=pid)
    if Cart.objects.filter(user=request.user).exists():
        cart = Cart.objects.get(user=request.user)
    else:
        cart = Cart.objects.create(user=request.user)
    if CartItem.objects.filter(cart=cart, product=product).exists():
        item  = CartItem.objects.get(cart=cart, product=product)
        item.qty += 1
        item.save()
    else: 
        item = CartItem.objects.create(cart=cart, product=product)
    return HttpResponse('added')

@login_required
def remove_product_from_cart(request, pid):
    product = Product.objects.get(id=pid)
    cart = Cart.objects.get(user=request.user)
    item = CartItem.objects.get(cart=cart, product=product)
    item.delete()
    return HttpResponse('<tr><td colspan="5" class="text-center">Item removed</td></tr>')

@login_required
def view_cart(request):
    if Cart.objects.filter(user=request.user).exists():
        cart = Cart.objects.get(user=request.user)
        return render(request, 'cart/view_cart.html',{
            'cart': cart,
            'items':CartItem.objects.filter(cart=cart) # should be filtered by user
        })
    messages.error(request, 'You do not any item in the cart')
    return redirect(request.META.get('HTTP_REFERER', '/'))
@login_required
def checkout(request):
    if Cart.objects.filter(user=request.user).exists():
        cart = Cart.objects.get(user=request.user)
        cart.delete()
    return render(request, 'cart/checkout.html')