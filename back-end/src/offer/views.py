from .models import *
from django.shortcuts import render, redirect
from product.models import Product

import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django.conf import settings

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

def getOfferPDF(request):

    products = []

    # Получаем продукцию
    if request.session.get('products', False):
        for session_product in request.session['products']:
            product = Product.objects.get(pk=session_product['product'])
            products.append(product)


    # Генерация PDF файла 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="offer.pdf"'

    pdfmetrics.registerFont(TTFont('Exo2-Medium', 'siteapp/static/font/Exo2-Medium.ttf'))    

    p = canvas.Canvas(response, pagesize=A4)
    p.setFont("Exo2-Medium", 14)

    p.drawString(50, 780, "Образец")
    p.drawString(50, 750, "КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ")
    y = 730

    p.setFont("Exo2-Medium", 8)

    p.drawString(50, y, "Наименование")
    p.drawString(320, y, "Серия")
    p.drawString(390, y, "Группа")
    p.drawString(480, y, "Сумма")
    p.line(50,y-5,550,y-5)
    y -= 25

    for inx,product in enumerate(products):
        p.drawString(50, y, product.title)
        p.drawString(320, y, product.series)
        p.drawString(390, y, product.group.title)
        p.drawString(480, y, "Нет")
        y -= 25

    p.drawString(440, y, "Итого:")
    p.drawString(480, y, "-")

    p.showPage()
    p.save()
    return response
    

def removeItem(request, id):
    
    product = Product.objects.get(pk=id)

    if request.session.get('products', False):
        for index, session_product in enumerate(request.session['products']):
            if (product.id == session_product['product']):
                del request.session['products'][index]
                request.session.modified = True

    return redirect('offer-show')