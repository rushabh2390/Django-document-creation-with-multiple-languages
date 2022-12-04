from django.contrib import admin
from django.conf import settings
from .models import Article
# Register your models here.
admin.site.register(Article)