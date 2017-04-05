from django.conf import settings

ARTICLES_PER_PAGE = getattr(settings, 'ARTICLE_PER_PAGE', 3)
BLOG_TITLE = getattr(settings, 'BLOG_TITLE', 'I Need A Good Name')
