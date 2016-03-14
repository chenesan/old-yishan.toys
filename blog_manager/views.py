from django.shortcuts import render
from django.views import generic
import blog.models

class IndexView(generic.TemplateView):
    template_name = 'blog_manager/index.html'

class ArticleListView(generic.ListView):
    context_object_name = 'article_list'
    template_name = 'blog_manager/article_list.html'
    model = blog.models.Article
