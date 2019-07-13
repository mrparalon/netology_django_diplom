from django.contrib import admin
from articles.models import Article, Author
from phones.models import Phone


class ArticleAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Phone, PhoneAdmin)
