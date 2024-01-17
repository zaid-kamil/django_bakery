from django.shortcuts import render
from inventory.models import Collection

def home(request):
    return render(request, 'home.html', context={
        'collections': Collection.objects.all()[:4] # get first 4 collections
    })


# about func -> about.html
def about(request):
    return render(request, 'about.html')

# contact func -> contact.html
def contact(request):
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        message = request.form.get('message')
        #  save to database with the Contact model
    return render(request, 'contact.html')

# gallery func -> gallery.html