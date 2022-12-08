from urllib import response
from django.test import TestCase, override_settings
from .models import Article
from django.utils.translation import get_language, activate
# Create your tests here.


class ArticleTestCase(TestCase):

    def setUp(self):
        article = Article()
        article.title = '{"title_en": "foo", "title_fr": "bar", "title_es": "xyz"}'
        article.save()

    def test_for_english_language(self):
        url = '/articles/'
        response = self.client.get(url, follow=True)
        body = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('foo', body)

    @override_settings(LANGUAGE_CODE='fr', LANGUAGES=(('fr', 'French'),))
    def test_for_french_language(self):
        url = '/articles/'
        response = self.client.get(url, follow=True)
        body = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('bar', body)

    @override_settings(LANGUAGE_CODE='es', LANGUAGES=(('es', 'Spanish'),))
    def test_for_spanish_language(self):
        url = '/articles/'
        response = self.client.get(url, follow=True)
        body = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('xyz', body)

    @override_settings(LANGUAGE_CODE='br', LANGUAGES=(('br', 'Germany'),))
    def test_for_germany_when_no_language(self):
        url = '/articles/'
        response = self.client.get(url, follow=True)
        body = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('foo', body)

    @override_settings(LANGUAGE_CODE='br', LANGUAGES=(('br', 'Germany'),))
    def test_for_germany_language(self):
        Article.objects.filter(pk=1).update(
            title='{"title_en": "foo", "title_fr": "bar", "title_es": "xyz", "title_br":"abc"}')
        url = '/articles/'
        response = self.client.get(url, follow=True)
        body = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('abc', body)