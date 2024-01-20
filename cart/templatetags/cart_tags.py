from cart.models import Cart, CartItem
from django.template import Library

register = Library()

@register.simple_tag()
def count_cart_items():
    return CartItem.objects.count()