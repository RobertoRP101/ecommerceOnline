from django.shortcuts import render
from store.models import Product
from .models import Cart
# Create your views here.

def cart_id():
    pass

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get()
    except:
        pass

def cart(request):
    return render(request, 'store/cart.html')