from .models import *
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json

def showProducts(request):

    group_products = GroupProduct.objects.all()
    
    # if request.session.get('products', False):
    #     for lt in list_products:
    #         for product in lt:
    #             for session_product in request.session['products']:
    #                 if (product.id == session_product['product']):
    #                     product.added = True

    return render(
        request,
        'products.html',
        context={
            'group_products': group_products
        }
    )

def addProduct(request, id):
    product = Product.objects.get(pk=id)

    products_list = []

    if not 'products' in request.session or not request.session['products']:
        request.session['products'] = [{ 'product': product.id }]
    else:
        products_list = request.session['products']
        products_list.append({ 'product': product.id })
        request.session['products'] = products_list

    return redirect('product-all')

def removeProduct(request, id):
    product = Product.objects.get(pk=id)

    if request.session.get('products', False):
        for index, session_product in enumerate(request.session['products']):
            if (product.id == session_product['product']):
                del request.session['products'][index]
                request.session.modified = True
                
    return redirect('product-all')


def showProduct(request, id):

    product = Product.objects.get(pk=id)
    solutions = product.solutions_set.all()
    specifications = product.specifications_set.all()

    # TODO (говно код) удаление продукта из сессии 
    if request.method == 'GET':  
        data = request.GET.copy()     
        if (data.get('remove')):
            if request.session.get('products', False):
                for index, session_product in enumerate(request.session['products']):
                    if (product.id == session_product['product']):
                        del request.session['products'][index]
                        request.session.modified = True


    # Добавление продукта в сессию
    if request.method == 'POST':      
        products_list = []

        if not 'products' in request.session or not request.session['products']:
            request.session['products'] = [{ 'product': product.id }]
        else:
            products_list = request.session['products']
            products_list.append({ 'product': product.id })
            request.session['products'] = products_list

    # Проверка существует ли текущий продукт в сесии, если существует отмечаем его
    if request.session.get('products', False):
        for session_product in request.session['products']:
            if (product.id == session_product['product']):
                product.added = True

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