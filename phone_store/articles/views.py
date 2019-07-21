from django.shortcuts import render
from articles.models import Article


def show_article(request, slug):
    article = Article.objects.prefetch_related('products').get(slug=slug)
    # article.prefetch_related('author')
    # article.prefetch_related('phones')
    products = article.products.all()
    context = {'article': article,
               'products': products}
    print(article.title)
    return render(request,
                  'article.html',
                  context=context)
