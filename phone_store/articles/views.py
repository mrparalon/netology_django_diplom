from django.shortcuts import render
from articles.models import Article


def show_article(request, slug):
    article = Article.objects.prefetch_related('phones').get(slug=slug)
    # article.prefetch_related('author')
    # article.prefetch_related('phones')
    phones = article.phones.all()
    context = {'article': article,
               'phones': phones}
    print(article.title)
    return render(request,
                  'article.html',
                  context=context)
