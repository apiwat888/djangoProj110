from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
   return render(request,'home.html')

def edu(request):
    return render(request,'edu.html')

def interests(request):
    return render(request,'interests.html')

def product(request):
    return render(request,'product.html')

def rolemodel(request):
    return render(request,'rolemodel.html')