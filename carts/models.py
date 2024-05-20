from django.db import models

# Create your models here.

class Cart(models.Models):
    cart_id = models.CharField(max_length=250, blank=True)
