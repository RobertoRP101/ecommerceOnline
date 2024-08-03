from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True)
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)