from django.shortcuts import render
from blog import models

# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def page_content(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'page_content.html',{'article': article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request,'edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request,'edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article_id = request.POST.get('article_id')
    if str(article_id) == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request,'page_content.html',{'article': article})