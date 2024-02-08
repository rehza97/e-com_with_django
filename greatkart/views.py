from django.http import HttpResponse
from django.shortcuts import render
from store.models import *

def home(reuqest):
    products = Product.objects.all().filter(is_available = True)
    
    context ={
        'products' :products 
    }
    return render(reuqest,'index.html',context)