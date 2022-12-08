import json
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language, activate
from .models import Article

def index(request):
    # activate('fr')
    article = Article.objects.first()

    title_data = json.loads(article.title)
    if 'title_'+get_language() in title_data:
        return HttpResponse(title_data['title_'+get_language()])
    else:
        return HttpResponse(title_data['title_en'])

def french_title(request):
    activate('fr')
    article = Article.objects.first()

    title_data = json.loads(article.title)
    if 'title_'+get_language() in title_data:
        return HttpResponse(title_data['title_'+get_language()])
    else:
        return HttpResponse(title_data['title_en'])

def spanish_title(request):
    activate('es')
    article = Article.objects.first()

    title_data = json.loads(article.title)
    if 'title_'+get_language() in title_data:
        return HttpResponse(title_data['title_'+get_language()])
    else:
        return HttpResponse(title_data['title_en'])