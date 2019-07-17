from django.shortcuts import render
from articles.models import Article


def show_index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request,
                  'index.html',
                  context=context)