from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse

def show(request):

    return render(
        request,
        'contact.html',
        context={
           
        }
    )