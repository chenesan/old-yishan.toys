from . import models, settings


def show_categories(request):
    return {
        'categories': models.Category.objects.all(),
    }


def show_tags(request):
    return {
        'tags': list(set(models.Tag.objects.filter(article__hide=False)))
    }


def show_blog_title(request):
    return {
        'blog_title': settings.BLOG_TITLE,
    }
