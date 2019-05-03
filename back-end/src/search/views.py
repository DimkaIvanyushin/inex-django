from .models import *
from django.contrib.postgres.search import SearchVector
from django.db.models import Count, Q 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product


def show(request):

    products_list = []

    if request.method == 'POST':
        search_string = request.POST.get('search_string')

        if search_string:
            products_list = Product.objects.filter(Q(title__icontains=str(search_string)) | Q(series__icontains=str(search_string)))
            
            return render(
                request,
                'search.html',
                context={
                    'products': products_list
                }
            )

    return render(
        request,
        'search.html',
        context={
            'test': True
        }
    )
    # Нет результатов для "qwf"