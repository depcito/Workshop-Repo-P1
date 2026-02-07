from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    searchterm = request.GET.get('searchMovie')
    if searchterm:
        movies = Movie.objects.filter(title__icontains=searchterm)
    else:
        movies=Movie.objects.all()
    return render(request, 'home.html', {'searchterm': searchterm, 'movies': movies})
    return render(request, 'home.html', {'name': 'Samuel Hernando Echeverri Castrillon'})

    #return HttpResponse("Welcome to Home Page </h1>")
def about(request):
    #return HttpResponse("Welcome to About Page </h1>")
    return render(request, 'about.html')
