from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='manage_index'),
    url(r'^article-list/$', views.ArticleListView.as_view(), name='manage_article_list'),
]
