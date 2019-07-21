from django.shortcuts import render, HttpResponse
from articles.models import Article
from shop.models import Product


def show_index(request):
    articles = Article.objects.all()
    products = Product.objects.order_by('?')[:3]
    context = {'articles': articles,
               'products': products}
    return render(request,
                  'index.html',
                  context=context)


def show_product(request, category, id):
    product = Product.objects.get(id=id)
    add_info = product.add_info.first()
    print(add_info)
    context = {'product': product,
               'add_info': add_info}
    return render(request,
                  'phone.html',
                  context=context)
