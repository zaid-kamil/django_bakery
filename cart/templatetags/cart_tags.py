from cart.models import Cart, CartItem
from django.template import Library

register = Library()

@register.simple_tag(takes_context=True)
def count_cart_items(context):
    request = context.get('request')
    user = request.user
    if user.is_authenticated:
        if Cart.objects.filter(user=user).exists():
            cart = Cart.objects.get(user=user)
            return CartItem.objects.filter(cart=cart).count()
    return 0