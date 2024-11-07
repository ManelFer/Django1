from django.http import HttpResponse
#from django.shortcuts import render

def blog(request):
    return HttpResponse('blog do app alterado')

def exemplo(request):
    return HttpResponse('Exemplo do app alterado')

# Create your views here.
