from django.shortcuts import render
from .models import Collection, Product, ProductImage

def collection(request, id):
    c = Collection.objects.get(id=id)
    return render(request, 'inventory/collection.html', context={
        'collection': c,
        'products': Product.objects.filter(collection=c)
    })

def collection_list(request):
    return render(request, 'inventory/collection_all.html', context={
        'collections': Collection.objects.all()
    })

def product_list(request):
    return render(request, 'inventory/product_all.html', context={
        'products': Product.objects.all(),
        'collections': Collection.objects.all(),
    })

def product(request, id):
    p = Product.objects.get(id=id)
    return render(request, 'inventory/product.html', context={
        'product': p,
        'images': ProductImage.objects.filter(product=p)
    })