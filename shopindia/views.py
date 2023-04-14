from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def clients(request):
    return render(request,'clients.html')

def contact(request):
    return render(request,'contact.html')