from django.shortcuts import render , get_object_or_404
from .models import *
from category.models import *
# Create your views here.
def store(request,category_slug=None):
    categories = None
    products = None
    if  category_slug != None:
       
        categories = get_object_or_404(Category , slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_counts = products.count()
    else:    
        products = Product.objects.all()
        
        products_counts = products.count()
    
    context={
        'products' : products,
        'categories' : categories,
        'products_counts' : products_counts,
        
        
    }
    return render(request, 'store.html',context)

def product_details(request,product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'product' : product
    }
    return render(request , 'product-detail.html',context)
    