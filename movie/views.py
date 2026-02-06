from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome to Home Page </h1>")
def about(request):
    #return HttpResponse("Welcome to About Page </h1>")
    return render(request, 'about.html')