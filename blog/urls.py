from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/([\w]+)$',
        views.CategoryView.as_view(), name='category'),
    url(r'^entry/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)$',
        views.EntryView.as_view(), name='entry'),
    url(r'^tag/([\w]+)$',
        views.TagView.as_view(), name='tag'),
]
