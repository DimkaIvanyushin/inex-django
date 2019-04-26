from .models import *
from django.shortcuts import render, redirect
from product.models import Product

def show(request):

    products = []

    if request.session.get('products', False):
        for session_product in request.session['products']:
            product = Product.objects.get(pk=session_product['product'])
            products.append(product)
                        
    return render(
        request,
        'offer.html',
         context={
            'products': products
        }
    )

def removeItem(request, id):
    
    product = Product.objects.get(pk=id)

    if request.session.get('products', False):
        for index, session_product in enumerate(request.session['products']):
            if (product.id == session_product['product']):
                del request.session['products'][index]
                request.session.modified = True

    return redirect('offer-show')