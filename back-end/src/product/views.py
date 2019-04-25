from .models import *
from django.shortcuts import render
from django.core.serializers import serialize
import json

def showProducts(request):
    return render(
        request,
        'products.html'
    )

def showProduct(request, id):

    product = Product.objects.get(pk=id)
    solutions = product.solutions_set.all()
    specifications = product.specifications_set.all()

    request.session['product'] = serialize('json', [product])

    return render(
        request,
        'product.html',
        context={
            'product': product,
            'solutions': solutions,
            'specifications': specifications
        }
    )

def showGroupProduct(request, id):

    print("===============================")
    if request.session.get('product', False):
        product = json.dumps(request.session['product'])
        print(product)

    group_product = GroupProduct.objects.get(pk=id)
    products = group_product.product_set.all()

    return render(
        request,
        'products-group.html',
        context={
            'group_product': group_product,
            'products': products
        }
    )
