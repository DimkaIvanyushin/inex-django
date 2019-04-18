from .models import *
from django.shortcuts import render

def showProducts(request):

    group_products = GroupProduct.objects.all()

    return render(
        request,
        'products.html',
        context={
            'group_products': group_products
        }
    )

def showProduct(request, id):

    product = Product.objects.get(pk=id)
    solutions = product.solutions_set.all()
    specifications = product.specifications_set.all()

    return render(
        request,
        'service.html',
        context={
            'product': product,
            'solutions': solutions,
            'specifications': specifications
        }
    )

def showGroupProduct(request, id):

    group_product = GroupProduct.objects.get(pk=id)
    products = group_product.product_set.all()

    return render(
        request,
        'services-list.html',
        context={
            'group_product': group_product,
            'products': products
        }
    )
