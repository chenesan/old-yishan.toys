from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views import generic
from . import models


class IndexView(generic.ListView):
    context_object_name = 'articles'
    template_name = 'article_title_list.html'

    def get_queryset(self):
        return models.Article.objects.filter(
            post_time__lte=timezone.now(),
            hide=False
        ).order_by('-post_time')


class EntryView(generic.DetailView):
    model = models.Article
    template_name = 'entry.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.filter(
            article=context['article']
        )
        # add hit count
        self.object.view_count += 1;
        return context


class TagView(generic.ListView):
    model = models.Article
    template_name = 'tag.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.tag = get_object_or_404(
            models.Tag, name=self.args[0]
        )
        return models.Article.objects.filter(
            tags__name=self.tag,
            hide=False
        ).order_by('-post_time')

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
