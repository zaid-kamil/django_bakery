from django.shortcuts import render
from inventory.models import Collection

def home(request):
    return render(request, 'home.html', context={
        'collections': Collection.objects.all()[:4] # get first 4 collections
    })


# about func -> about.html

# contact func -> contact.html

# gallery func -> gallery.html