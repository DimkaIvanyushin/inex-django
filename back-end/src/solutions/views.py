from django.shortcuts import render
from .models import *

def showSolutions(request):

    return render(
        request,
        'solution-list.html',
        context={
           
        }
    )


def showSolutionId(request, id):

    return render(
        request,
        'solution.html',
        context={
           
        }
    )