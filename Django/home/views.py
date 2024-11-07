from django.http import HttpResponse
#from django.shortcuts import render


def home(request):
    return HttpResponse('home do app alterado')

# Create your views here.
