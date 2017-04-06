from .base import *


DEBUG = False

# fill in your hosts
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'production.cnf'),
        },
    }
}

# Error
# fill in admins and manager info.
ADMINS = []

MANAGERS = []

GOOGLE_ANALYTICS_PROPERTY_ID = get_env_var('GOOGLE_ANALYTICS_PROPERTY_ID')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
