from django.shortcuts import render
from django.http import HttpResponse

def portfolio(request):
    return render(request, 'home/portfolio.html')


def services(request):
    return render(request, 'home/services.html')


def contact(request):
    return render(request, 'home/contact.html')
