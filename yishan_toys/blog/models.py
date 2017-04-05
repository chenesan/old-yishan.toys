from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/tag/{name}/'.format(name=self.name)

class Article(models.Model):
    """
    TODO:
    * where
    """
    author = models.CharField(max_length=25, default="")
    content = models.TextField()
    hide = models.BooleanField(default=False)
    post_time = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=50)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=50)
    view_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/entry/{id}/{slug}/'.format(id=self.id, slug=self.slug)
