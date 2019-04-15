from .models import *
from django.shortcuts import render


def showProduct(request, id):

    product = Product.objects.get(pk=id)

    return render(
        request,
        'service.html',
        context={
            'product': product
        }
    )


def showGroupProduct(request, id):

    group_product = GroupProduct.objects.get(pk=id)

    return render(
        request,
        'services-list.html',
        context={
            'group_product': group_product
        }
    )
