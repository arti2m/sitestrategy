from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import get_object_or_404

from .models import *

# Create your views here.
menu = ['О Создании стратегии', 'О Проектном офисе','Статьи', 'Новости и события', 'Идеи',
        'Интерактивная карта', 'Национальные проекты', 'Эксперты и мнения']
menuverh = ['О Создании стратегии', 'О Проектном офисе']
menuniz = ['Статьи', 'Новости и события', 'Идеи', 'Интерактивная карта', 'Национальные проекты', 'Эксперты и мнения']
newsall = News.objects.filter().order_by('-datetime')
news2 = newsall[1]
news3 = newsall[2]

chronic = Chronic.objects.filter().order_by('-datetime')
chronic1 = chronic[0]
chronic2 = chronic[1]
chronic3 = chronic[2]


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
    mainnews = News.objects.filter(mainNews=True).order_by('-pk')[0]
    news = News.objects.all().order_by('-datetime')
    paginator = Paginator(news, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tags.objects.all()
    return render(request, 'websitestrategy/news.html',{'news' : news,
                                                        # 'page_obj': page_obj,
                                                        'tags' : tags,
                                                        'mainnews' : mainnews,
                                                        'title' : 'Новости: Главная страница',
                                                        'news2' : news2,
                                                        'news3' : news3,
                                                        'chronic1':chronic1,
                                                        'chronic2': chronic2,
                                                        'chronic3': chronic3,
                                                        'menu' : menu})

def show_news(request, news_slug):
    news = get_object_or_404(News, slug = news_slug)
    mainnews = News.objects.filter(mainNews=True).order_by('-pk')[0]
    context = {'news' : news,
               # 'page_obj': page_obj,
               # 'tags' : tags,
               'mainnews' : mainnews,
               'title' : 'Новости: Главная страница',
               'news2' : news2,
               'news3' : news3,
               'chronic1':chronic1,
               'chronic2': chronic2,
               'chronic3': chronic3,
               'menu' : menu}

    return render(request,'websitestrategy/show_news.html', context=context)