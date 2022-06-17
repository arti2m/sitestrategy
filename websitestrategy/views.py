from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import *

# Create your views here.
menu = ['О Создании стратегии', 'О Проектном офисе','Статьи', 'Новости и события', 'Идеи',
        'Интерактивная карта', 'Национальные проекты', 'Эксперты и мнения']
menuverh = ['О Создании стратегии', 'О Проектном офисе']
menuniz = ['Статьи', 'Новости и события', 'Идеи', 'Интерактивная карта', 'Национальные проекты', 'Эксперты и мнения']

def index(request):
    return render(request, 'websitestrategy/index.html')

def cats(request,cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'Страница Категории,Категория{cat}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена 404 ошибка')

def about(request):
    return render(request, 'websitestrategy/about-strategy.html')

def news(request):
    news = News.objects.all()
    tags = Tags.objects.all()
    return render(request, 'websitestrategy/news.html',{'news' : news,
                                                        'tags' : tags,
                                                        'title' : 'Новости: Главная страница',
                                                        'menu' : menu})