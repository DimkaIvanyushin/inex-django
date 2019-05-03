from .models import *
from django.shortcuts import render, redirect
from product.models import Product

import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

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
    p.setFont("Exo2-Medium", 12)

    logo = ImageReader('http://localhost:8080/static/images/logo.jpg')

    p.drawImage(logo, 10, 10, mask='auto')

    p.drawString(330, 780, "Витебское республиканское унитарное")
    p.drawString(350, 765, "предприятие электроэнергетики")
    p.drawString(400, 750, "«Витебскэнерго»")

    p.drawString(380, 730, "Филиал «Учебный центр»")

    p.drawString(330, 710, "ул. Полярная, 38А, 210017, г. Витебск")

    p.drawString(330, 695, "тел.: +375 (212) 49 28 59 – приёмная")
    p.drawString(380, 690, "факс: +375 (212) 36 06 20")
    p.drawString(360, 680, "е-mail: uc@vitebsk.energo.by")

    p.drawString(330, 660, "р/с  BY76BPSB30121160110139330000")
    p.drawString(330, 650, "в ОАО «БПС-Сбербанк»")
    p.drawString(330, 640, "г. Минск, б-р Мулявина, 6  ")
    p.drawString(330, 630, "SWIFT BIC: BPSBBY2X УНП 300000252")

    p.drawString(130, 620, "Коммерческое предложение")


    # p.drawString(50, 780, "Образец")
    # p.drawString(50, 750, "КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ")
    # y = 730

    # p.setFont("Exo2-Medium", 8)

    # p.drawString(50, y, "Наименование")
    # p.drawString(320, y, "Серия")
    # p.drawString(390, y, "Группа")
    # p.drawString(480, y, "Сумма")
    # p.line(50,y-5,550,y-5)
    # y -= 25

    # for inx,product in enumerate(products):
    #     p.drawString(50, y, product.title)
    #     p.drawString(320, y, product.series)
    #     p.drawString(390, y, product.group.title)
    #     p.drawString(480, y, "Нет")
    #     y -= 25

    # p.drawString(440, y, "Итого:")
    # p.drawString(480, y, "-")

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

def removeItemAll(request):
    del request.session['products']
    
    return redirect('offer-show')