from django.forms import ModelForm, Textarea

from pagedown.widgets import PagedownWidget

from blog import models

class ArticleForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ['content', 'title', 'slug', 'tags', 'hide']
        widgets = {
            'content': PagedownWidget()
        }
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['tags'].required = False
