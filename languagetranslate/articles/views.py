from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import get_language, activate


def index(request):
    activate('fr')
    return HttpResponse(get_language())