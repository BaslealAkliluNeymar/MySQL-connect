from django.shortcuts import render
from .models import Products
# Create your views here.

def product_detail_view(request,*args,**kwargs):
    obj = Products.objects.get(id=7)
    context = {
        "title":obj.title,
        "description":obj.description,
        "price":obj.price
    }
    return render(request,"products/detail.html",context)


