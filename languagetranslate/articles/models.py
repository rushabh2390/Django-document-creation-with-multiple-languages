from django.db import models
import jsonfield
# Create your models here.


class Article(models.Model):
    title = jsonfield.JSONField()
