from django.shortcuts import render
from .models import News

def news(request):
    newss = News.objects.all() .order_by('-date') # ordena las noticias por fecha de forma descendente
    return render(request, 'news.html', {'newss': newss})
