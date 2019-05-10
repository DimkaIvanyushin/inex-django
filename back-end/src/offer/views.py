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
            product.count = session_product['count']
            products.append(product)
                      
    return render(
        request,
        'offer.html',
         context={
            'products': products
        }
    )

def test():
    print('HELLO')

def getOfferPDF(request):

    products = []

    # Получаем продукцию
    if request.session.get('products', False):
        for session_product in request.session['products']:
            product = Product.objects.get(pk=session_product['product'])
            product.count = session_product['count']
            products.append(product)


    # Генерация PDF файла 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="offer.pdf"'

    pdfmetrics.registerFont(TTFont('Exo2-Medium', 'siteapp/static/font/Exo2-Medium.ttf'))
    pdfmetrics.registerFont(TTFont('Exo2-Bold', 'siteapp/static/font/Exo2-Bold.ttf'))    

    p = canvas.Canvas(response, pagesize=A4)
    p.setFont("Exo2-Medium", 12)

    logo = ImageReader('siteapp/static/images/logo.jpg')

    p.drawImage(logo, 70, 650, 165, 110)

    p.drawString(300, 780, "Витебское республиканское унитарное")
    p.drawString(320, 765, "предприятие электроэнергетики")
    p.drawString(370, 750, "«Витебскэнерго»")

    p.setFont("Exo2-Bold", 12)
    p.drawString(350, 730, "Филиал «Учебный центр»")
    p.setFont("Exo2-Medium", 12)

    p.drawString(300, 710, "ул. Полярная, 38А, 210017, г. Витебск")

    p.drawString(300, 695, "тел.: +375 (212) 49 28 59 – приёмная")
    p.drawString(350, 680, "факс: +375 (212) 36 06 20")
    p.drawString(330, 665, "е-mail: uc@vitebsk.energo.by")

    p.drawString(300, 640, "р/с  BY76BPSB30121160110139330000")
    p.drawString(350, 625, "в ОАО «БПС-Сбербанк»")
    p.drawString(340, 610, "г. Минск, б-р Мулявина, 6  ")
    p.drawString(300, 595, "SWIFT BIC: BPSBBY2X УНП 300000252")

    p.setFont("Exo2-Bold", 16)
    p.drawString(180, 555, "Коммерческое предложение")
    p.setFont("Exo2-Medium", 12)

    y = 500
    p.setFont("Exo2-Medium", 12)

    p.drawString(50, y, "№")
    p.drawString(80, y, "Наименование")
    p.drawString(350, y, "Кол.")
    p.drawString(380, y, "Группа")
    p.drawString(480, y, "Сумма, BYN")
    p.line(50, y-5, 550, y-5)
    y -= 25

    res_sum = 0

    for inx,product in enumerate(products):
        p.drawString(50, y, str(inx + 1))
        p.drawString(80, y, product.title[:39])
        p.drawString(350, y, str(product.count))
        p.drawString(380, y, product.group.title[:15])
        price_product = product.count * product.price
        p.drawString(520, y, str(price_product))
        y -= 25
        res_sum += price_product

    p.line(50, y, 550, y)
    y -= 25
    p.setFont("Exo2-Bold", 12)
    p.drawString(480, y, "Итого:")
    p.drawString(520, y, str(res_sum))

    p.showPage()
    p.save()
    return response
    
    # TODO Переделать с self
def getAllOfferPDF(request):
    products = []

    products = Product.objects.all()

    # Генерация PDF файла 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="offer.pdf"'

    pdfmetrics.registerFont(TTFont('Exo2-Medium', 'siteapp/static/font/Exo2-Medium.ttf'))
    pdfmetrics.registerFont(TTFont('Exo2-Bold', 'siteapp/static/font/Exo2-Bold.ttf'))    

    p = canvas.Canvas(response, pagesize=A4)
    p.setFont("Exo2-Medium", 12)

    logo = ImageReader('siteapp/static/images/logo.jpg')

    p.drawImage(logo, 70, 650, 165, 110)

    p.drawString(300, 780, "Витебское республиканское унитарное")
    p.drawString(320, 765, "предприятие электроэнергетики")
    p.drawString(370, 750, "«Витебскэнерго»")

    p.setFont("Exo2-Bold", 12)
    p.drawString(350, 730, "Филиал «Учебный центр»")
    p.setFont("Exo2-Medium", 12)

    p.drawString(300, 710, "ул. Полярная, 38А, 210017, г. Витебск")

    p.drawString(300, 695, "тел.: +375 (212) 49 28 59 – приёмная")
    p.drawString(350, 680, "факс: +375 (212) 36 06 20")
    p.drawString(330, 665, "е-mail: uc@vitebsk.energo.by")

    p.drawString(300, 640, "р/с  BY76BPSB30121160110139330000")
    p.drawString(350, 625, "в ОАО «БПС-Сбербанк»")
    p.drawString(340, 610, "г. Минск, б-р Мулявина, 6  ")
    p.drawString(300, 595, "SWIFT BIC: BPSBBY2X УНП 300000252")

    p.setFont("Exo2-Bold", 16)
    p.drawString(180, 555, "Коммерческое предложение")
    p.setFont("Exo2-Medium", 12)

    y = 500
    p.setFont("Exo2-Medium", 12)

    p.drawString(50, y, "№")
    p.drawString(80, y, "Наименование")
    p.drawString(350, y, "Кол.")
    p.drawString(380, y, "Группа")
    p.drawString(480, y, "Сумма, BYN")
    p.line(50, y-5, 550, y-5)
    y -= 25

    res_sum = 0

    for inx,product in enumerate(products):
        p.drawString(50, y, str(inx + 1))
        p.drawString(80, y, product.title[:39])
        p.drawString(350, y, str(1))
        p.drawString(380, y, product.group.title[:15])
        price_product = 1 * product.price
        p.drawString(520, y, str(price_product))
        y -= 25
        res_sum += price_product

    p.line(50, y, 550, y)
    y -= 25
    p.setFont("Exo2-Bold", 12)
    p.drawString(480, y, "Итого:")
    p.drawString(520, y, str(res_sum))

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

def incItem(request, id):
    if request.session.get('products', False):
        for index, session_product in enumerate(request.session['products']):
            if (int(session_product['product']) == int(id)):
                request.session['products'][index]['count'] += 1
                request.session.modified = True

    return redirect('offer-show')

def decItem(request, id):
    if request.session.get('products', False):
        for index, session_product in enumerate(request.session['products']):
            if int(session_product['product']) == int(id):
                request.session['products'][index]['count'] -= 1
                request.session.modified = True

    return redirect('offer-show')

def removeItemAll(request):
    del request.session['products']
    
    return redirect('offer-show')