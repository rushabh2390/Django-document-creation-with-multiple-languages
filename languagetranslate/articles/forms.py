from django import forms
from .models import Article
from django.conf import settings

support_language = ["title_"+x[0] for x in settings.LANGUAGES]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('title',)

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for key in support_language:
            self.fields[key] = forms.CharField(max_length=200, label=key)
        print("-----------------------------------------------------------")
        print(self.fields)
        print("-----------------------------------------------------------")
