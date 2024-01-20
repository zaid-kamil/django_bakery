from django.urls import path
from .views import *
urlpatterns = [
    path('cart/add/<int:pid>', add_product_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pid>', remove_product_from_cart, name='remove_from_cart'),
    path('cart/view', view_cart, name='view_cart'),
    path('cart/checkout', checkout, name='checkout'),
]