from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print('hello django')
    return HttpResponse('<h1>hello django</h1>')