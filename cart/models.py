from django.db import models

# Create your models here.
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Cart({self.id})'
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('inventory.Product', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"cart item ({self.product.name})"
    