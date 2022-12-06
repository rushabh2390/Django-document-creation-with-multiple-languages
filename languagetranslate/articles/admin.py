from django.contrib import admin
from .models import Article
from .forms import ArticleForm
from django.conf import settings

support_language = ["title_"+x[0] for x in settings.LANGUAGES]


class ArticleFormAdmin(admin.ModelAdmin):
    form = ArticleForm
    def get_fieldsets(self, request, obj=None):
        fieldsets = super(ArticleFormAdmin, self).get_fieldsets(request, obj)
        fieldsets[0][1]['fields'] += ['text_en']
        return fieldsets

# Register your models here.
admin.site.register(Article, ArticleFormAdmin)
