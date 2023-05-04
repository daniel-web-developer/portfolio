from django.shortcuts import render
from .models import Article


# Create your views here.
def index(request):
    return render(request, "blog/index.html",{
        "articles": Article.objects.all()
    })

def article(request, article_id):
    article = Article.objects.get(pk = article_id)
    return render(request, "blog/article.html", {
        "article": article
    })