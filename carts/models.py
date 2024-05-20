from django.db import models

# Create your models here.

class Cart(models.Models):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    
class CartItem(models.Model):
    pass