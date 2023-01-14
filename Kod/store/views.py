from django.shortcuts import render, get_object_or_404

from shop.models import Product, Category

# Create your views here.
def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]

    return render(request, 'store/frontpage.html',{
        'products': products
    })

def about(request):
    return render(request, 'store/about.html')