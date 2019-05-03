from django.shortcuts import render
from product.models import Product
from solutions.models import Solutions
from django.db.models import Q 
from django.http import HttpResponse, JsonResponse
from django.core import serializers

import json

def search(request):
    search_query = request.GET.get('search_query', '').capitalize()

    if search_query: 

        products = Product.objects.filter(Q(title__icontains=search_query) | Q(series__icontains=search_query))
        solutions = Solutions.objects.filter(industry__icontains = search_query)

        results = []
        for product in products:
            results.append({
                'title': product.title[:30] + '...',
                'title_href': product.get_absolute_url(),
                'category': product.group.title,
                'category_href': product.group.get_absolute_url(),
                'image': product.images.first().image.url
            })

        for solution in solutions:
            results.append({
                'title': solution.industry[:30] + '...',
                'title_href': solution.get_absolute_url(),
                'category': 'Решения',
                'category_href': '/solutions/all',
                'image': solution.img.url
            })

        data = json.dumps(results)
        return HttpResponse(data, 'application/json')