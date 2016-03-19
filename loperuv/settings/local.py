from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-75310497-1'

