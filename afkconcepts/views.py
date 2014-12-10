from django.shortcuts import render
from django.http import HttpResponse

def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
