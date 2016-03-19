from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='manage_index'),
    url(r'^article-list/$', views.ArticleListView.as_view(), name='manage_article_list'),
    url(r'^article-list/create/$', views.CreateArticleView.as_view(), name='manage_create_article'),
    url(r'^article-list/delete/(?P<pk>[0-9]+)/$', views.DeleteArticleView.as_view(), name='manage_delete_article'),
    url(r'^article-list/update/(?P<pk>[0-9]+)/$', views.EditArticleView.as_view(), name='manage_edit_article'),
    url(r'^logout/$', views.logout, name='manage_logout'),
]
