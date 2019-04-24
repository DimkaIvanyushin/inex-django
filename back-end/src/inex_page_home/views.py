from django.shortcuts import render
from product.models import Product
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json

def search(request):
    
    search_query = request.GET.get('search_query', '').capitalize()
    products = Product.objects.filter(title__startswith=search_query)
    results = []

    for product in products:
        results.append({
            'title': product.title,
            'title_href': product.get_absolute_url(),
            'category': product.group.title,
            'category_href': product.group.get_absolute_url(),
            'image': product.images.first().image.url
        })

    data = json.dumps(results)

    return HttpResponse(data, 'application/json')