from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request,'index.html',{'Articles': articles})



def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'article.html',{'Articles': article})


def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'Articles': article})




def edit_active(request):

    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id', '0')
    print (article_id)
    if article_id == '0':
        models.Article.objects.create(title=title,content=content)
        article = models.Article.objects.all()
        return render(request, 'index.html', {'Articles': article})

    articles = models.Article.objects.get(pk=article_id)
    articles.title = title
    articles.content = content
    articles.save()
    return render(request, 'article.html',{'Articles': articles})