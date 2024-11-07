from django.http import HttpResponse
#from django.shortcuts import render


def home(request):
    return HttpResponse('home do app')

# Create your views here.
