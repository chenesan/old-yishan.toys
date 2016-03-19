from django import template


register = template.Library()

@register.filter(name='first_n_paragraph')
@template.defaultfilters.stringfilter
def first_n_paragraph(article, n=1):
    return '\n'.join(article.split('\n')[:n])

