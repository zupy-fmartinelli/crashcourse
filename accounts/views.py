from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return HttpResponse('Home Page')

def products(request):
    return HttpResponse('Products Page')

def customers(request):
    return HttpResponse('Customer Page')
