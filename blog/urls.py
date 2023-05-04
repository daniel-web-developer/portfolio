from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
    path("<int:article_id>", views.article, name="article-number")
]