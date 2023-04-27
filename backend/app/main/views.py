from django.shortcuts import render
from article.models import Article

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def HomePage(request):
    trans = translate(language='ru')
    
    articles = Article.objects.all().order_by('-created_date')[:3]
    first_article = None
    second_article = None
    third_article = None

    if len(articles) >= 1:
        first_article = articles[0]
    if len(articles) >= 2:
        second_article = articles[1]
    if len(articles) >= 3:
        third_article = articles[2]

    context = {
        'first_article': first_article,
        'second_article': second_article,
        'third_article': third_article,
        'trans': trans
    }

    return render(request, 'main/home.html', context)


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text