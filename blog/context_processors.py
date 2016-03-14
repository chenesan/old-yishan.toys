from . import models, settings


def show_categories(request):
    return {
        'categories': models.Category.objects.all(),
    }


def show_tags(request):
    return {
        'tags': models.Tag.objects.all()
    }


def show_blog_title(request):
    return {
        'blog_title': settings.BLOG_TITLE,
    }
