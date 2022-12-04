from django import forms
from django.contrib import admin
from .models import Article

class ArticalForm(forms.ModelForm):

    class Meta:
        model = Article

class PersonAdmin(admin.ModelAdmin):
    exclude = ['age']
    form = ArticalForm