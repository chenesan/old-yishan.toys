import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Article, Tag


class IndexViewTest(TestCase):

    def setUp(self):
        Tag.objects.create(
            name="django"
        )
        Tag.objects.create(
            name="flask"
        )

    def test_index_not_show_future_article(self):

        article = Article.objects.create(
            title='future',
            content='article',
            post_time=timezone.now() + datetime.timedelta(days=10),
            author='me',
            slug='test-article',
        )
        article.tags = Tag.objects.filter(name='django')

        response = self.client.get('/')

        self.assertQuerysetEqual(response.context['articles'], [])

    def test_not_show_tags_have_no_unhided_articles(self):
        public_article = Article.objects.create(
            title='public',
            content='public article',
            post_time=timezone.now() + datetime.timedelta(days=10),
            author='me',
            slug='public-article',
            hide=False,
        )
        public_article.tags=Tag.objects.filter(name='django')

        hided_article = Article.objects.create(
            title='hided',
            content='hided article',
            post_time=timezone.now() + datetime.timedelta(days=10),
            author='me',
            slug='hided-article',
            hide=True,
        )
        hided_article.tags=Tag.objects.filter(name='flask')

        response = self.client.get('/')
        self.assertEqual(response.context['tags'][0].name, 'django')
