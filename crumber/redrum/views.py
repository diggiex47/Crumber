from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'redrum/dashboard.html')
def products(request):
    return render(request, 'redrum/products.html')
def customer(request):
    return render(request, 'redrum/customer.html')

