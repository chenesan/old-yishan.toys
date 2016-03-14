from __future__ import unicode_literals


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """
    TODO:
    * where
    * clicks
    """
    content = models.TextField()
    title = models.CharField(max_length=50)
    post_time = models.DateTimeField()
    author = models.CharField(max_length=25, default="")
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    hide = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    visitor = models.CharField(max_length=25)
    content = models.TextField()
    post_time = models.DateTimeField()
    article = models.ForeignKey(Article)
