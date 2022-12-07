from django.contrib import admin
from .models import Article
from .forms import ArticleForm
from django import forms
from django.conf import settings
import json

support_language = ["title_"+x[0] for x in settings.LANGUAGES]


class ArticleFormAdmin(admin.ModelAdmin):
    form = ArticleForm

    def get_fields(self, request, obj=None):
        fields = super(ArticleFormAdmin, self).get_fields(request, obj)
        if obj:
            new_dynamic_fields = []
            data = json.loads(obj.title)
            print("data is", data)
            for key in support_language:
                if key in data.keys():
                    new_dynamic_fields.append((key, forms.CharField(
                        max_length=200, label=key, initial=data[key])))
                else:
                    print("it came here")
                    new_dynamic_fields.append((
                        key, forms.CharField(max_length=200, label=key)))

        else:
            print("here")
            new_dynamic_fields = [
                (key, forms.CharField(max_length=200, label=key))
                for key in support_language
            ]
        for f in new_dynamic_fields:
            # `gf.append(f[0])` results in multiple instances of the new fields
            if f[0] not in fields:
                fields = fields + [f[0]]
                # updating base_fields seems to have the same effect
                print(f[1])
                self.form.declared_fields.update({f[0]: f[1]})
        return fields

    def save_model(self, request, obj, form, change=False):
        super().save_model(request, obj, form, change)
        articleform = ArticleForm(request.POST)
        if change:
            data = form.cleaned_data
            article = self.get_object(request, object_id=obj.id)
            article.title = json.dumps(data)
            print("oh", article.title)
            article.save()
        else:
            data = articleform.cleaned_data
            instance = Article()
            instance.title = json.dumps(data)
            instance.save()

    def get_object(self, request, object_id, from_field=None):
        obj = Article.objects.get(pk=object_id)
        return obj

        # super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Article, ArticleFormAdmin)
