from django.shortcuts import render

from .models import Solutions


def showSolutions(request):
    return render(
        request,
        'solution-list.html',

    )


def showSolutionId(request, id):

    solution = Solutions.objects.get(pk=id)
    products = solution.products.all()

    return render(
        request,
        'solution.html',
        context={
          'solution': solution,
          'products': products
        }
    )