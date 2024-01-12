from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to="collection", blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    food_choices = (
        (0, 'Egg'),
        (1, 'Eggless')
    )
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products")
    price = models.PositiveIntegerField(default=50)
    desc = models.TextField(null=True, blank=True)
    food_type = models.IntegerField(choices=food_choices, default=0)
    qty = models.FloatField(default=50.00, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    is_new = models.BooleanField(default=True)
    is_best_seller = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")

# python manage.py makemigrations
# python manage.py migrate