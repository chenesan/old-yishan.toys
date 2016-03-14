import datetime


from django.test import TestCase
from django.utils import timezone


from .models import Article, Category


class IndexViewTest(TestCase):
    def setUp(self):
        Category.objects.create(category='test_category')
        Article.objects.create(
            title='future',
            content='article',
            post_time=timezone.now() + datetime.timedelta(days=10),
            author='me',
            slug='test-article',
            category=Category.objects.get(id=1),
        )

    def test_index_not_show_future_article(self):

        response = self.client.get('/')

        self.assertQuerysetEqual(response.context['articles'], [])
