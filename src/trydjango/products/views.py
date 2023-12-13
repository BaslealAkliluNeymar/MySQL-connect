from django.shortcuts import render
from .models import Products
# Create your views here.

from .forms import ProductForm

def product_form(request,*args,**kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form":form
    }
    return render(request,"products/product_create.html",context)
def product_detail_view(request,*args,**kwargs):
    obj = Products.objects.get(id=7)
    context = {
        "object":obj
    }
    return render(request,"products/detail.html",context)


