from .base import *


DEBUG = True

ALLOWED_HOSTS = ['www.yishan.toys', 'yishan.toys']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(os.path.dirname(BASE_DIR), 'my_production.cnf'),
        },
    }
}

# Error
ADMINS = [
    ('chenesan', 'pipio1994@gmail.com'),
]

MANAGERS = [
    ('chenesan', 'pipio1994@gmail.com'),
]

GOOGLE_ANALYTICS_PROPERTY_ID = get_env_var('GOOGLE_ANALYTICS_PROPERTY_ID')

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
