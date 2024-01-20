from django.shortcuts import render, redirect, HttpResponse
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def add_product_to_cart(request, pid):
    return HttpResponse('added')

@login_required
def remove_product_from_cart(request, pid):
    return HttpResponse('removed')

@login_required
def view_cart(request):
    return render(request, 'cart/view_cart.html',{
        'items': CartItem.objects.all() # should be filtered by user
    })

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')