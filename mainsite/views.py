from django.shortcuts import render
from blog.models import Article
from .models import Project

# Create your views here.
def index(request):
    post = Article.objects.first() # It's first() instead of last() because the order is reversed by default in blog.models.py
    return render(request, 'index.html', {
        "article": post,
        "projects": Project.objects.all()
    })