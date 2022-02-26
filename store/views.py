from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from category.models import Category

from .models import product


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug )
        products = product.objects.filter(category=categories,is_available=True)
        product_count = products.count()
    else:
        products=product.objects.all().filter(is_available= True)

    products = product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html',context )

def product_detail(request,category_slug,product_slug):
    try:
        single_product = product.objects.get(category_slug=category_slug,slug= product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product':single_product,



    }

    return render(request,'store/product_detail.html',context)

