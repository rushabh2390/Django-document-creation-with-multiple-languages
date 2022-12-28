from django.contrib import admin
from .models import Article
from django import forms
from django.conf import settings
import json

support_language = [x[0] for x in settings.LANGUAGES]


class ArticleFormAdmin(admin.ModelAdmin):
    model = Article
    exclude = ('title','description')

    def get_fields(self, request, obj=None):
        modelFields = [f.name for f in Article._meta.get_fields() if f.name != "id"]
        fields = [x+"_"+y for x in modelFields for y in support_language]
        if obj:
            new_dynamic_fields = []
            for item in modelFields:
                data = json.loads(getattr(obj,item))
                for key in support_language:
                    if key in data:
                        new_dynamic_fields.append((item+"_"+key, forms.CharField(
                            max_length=200, label=item+"_"+key, initial=data[key])))
                    else:
                        new_dynamic_fields.append((
                            item+"_"+key, forms.CharField(max_length=200, label=item+"_"+key)))

        else:
            new_dynamic_fields = [
                (key, forms.CharField(max_length=200, label=key))
                for key in fields
            ]
        for f in new_dynamic_fields:
            if f[0] not in fields:
                fields = fields + [f[0]]

            self.form.declared_fields.update({f[0]: f[1]})

        return fields

    def save_model(self, request, obj, form, change=False):
        data = form.cleaned_data
        modelFields = [f.name for f in Article._meta.get_fields() if f.name != "id"]

        if change:
            article = self.get_object(request, object_id=obj.id)
        
        else:
            article = Article()
        
        for item in modelFields:
            itemvalues = {key.split("_")[1]:data[key] for key in data if key.startswith(item)}
            setattr(article, item, json.dumps(itemvalues))
            
        article.save()
# Register your models here.
admin.site.register(Article, ArticleFormAdmin)
