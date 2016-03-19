from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import generic

import blog.models
from .forms import ArticleForm

def login(request):
    if request.user.is_authenticated():
        return render(request, "blog_manager/index.html", locals())
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        auth.login(request, user)
        return render(request, "blog_manager/index.html", locals())
    else:
        return render(request, "blog_manager/login.html", locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/manage/", locals())

class EditArticleView(generic.edit.UpdateView):
    model = blog.models.Article
    form_class = ArticleForm
    template_name = 'blog_manager/edit_article.html'
    success_url = '/manage/article-list/'


class CreateArticleView(generic.edit.CreateView):
    form_class = ArticleForm
    template_name = 'blog_manager/edit_article.html'
    success_url = '/manage/article-list/'


class DeleteArticleView(generic.edit.DeleteView):
    context_object_name = 'article'
    model = blog.models.Article
    success_url = reverse_lazy('manage_article_list')
    template_name = 'blog_manager/delete_article.html'

class IndexView(generic.TemplateView):
    template_name = 'blog_manager/index.html'

class ArticleListView(generic.ListView):
    context_object_name = 'article_list'
    template_name = 'blog_manager/article_list.html'
    model = blog.models.Article

    def get_query_set(self):
        return model.objects.all().order_by('id')

