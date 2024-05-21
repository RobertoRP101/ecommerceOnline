from django.shortcuts import render
from store.models import Product

# Create your views here.


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

def cart(request):
    return render(request, 'store/cart.html')