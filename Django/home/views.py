#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home/index.html', {
        'text': 'Estamos na home'
    })
# Create your views here.
