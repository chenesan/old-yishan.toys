from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

class FaviconView(RedirectView):
    permanent = False
    url = staticfiles_storage.url('favicon.ico')
