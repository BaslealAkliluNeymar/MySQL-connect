from django.shortcuts import render
from .models import Products
# Create your views here.

def product_detail_view(request,*args,**kwargs):
    return render(request,"product/detail.html",{})


