from django.contrib import admin
from .models import Article
from django import forms
from django.conf import settings
import json

support_language = ["title_"+x[0] for x in settings.LANGUAGES]


class ArticleFormAdmin(admin.ModelAdmin):
    model = Article
    exclude = ('title',)

    def get_fields(self, request, obj=None):
        fields = super(ArticleFormAdmin, self).get_fields(request, obj)
        if obj:
            new_dynamic_fields = []
            data = json.loads(obj.title)
            for key in support_language:
                if key in data.keys():
                    new_dynamic_fields.append((key, forms.CharField(
                        max_length=200, label=key, initial=data[key])))
                else:
                    new_dynamic_fields.append((
                        key, forms.CharField(max_length=200, label=key)))

        else:
            new_dynamic_fields = [
                (key, forms.CharField(max_length=200, label=key))
                for key in support_language
            ]
        for f in new_dynamic_fields:
            if f[0] not in fields:
                fields = fields + [f[0]]

            self.form.declared_fields.update({f[0]: f[1]})

        return fields

    def save_model(self, request, obj, form, change=False):
        data = form.cleaned_data
        if change:
            article = self.get_object(request, object_id=obj.id)
            article.title = json.dumps(data)
            article.save()
        else:
            instance = Article()
            instance.title = json.dumps(data)
            instance.save()

# Register your models here.
admin.site.register(Article, ArticleFormAdmin)
