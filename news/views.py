from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news' : news})

def news_detail(request, key):
    article_detail = News.objects.get(pk=key)
    return render(request, 'news-detail.html', {'article_detail': article_detail})