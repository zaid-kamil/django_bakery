from django import template
from inventory.models import Collection, Product

register = template.Library()

@register.simple_tag()
def get_collections():
    return Collection.objects.all()


@register.simple_tag()
def get_products():
    return Product.objects.all()