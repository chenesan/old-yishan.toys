from .base import *

SECRET_KEY = "+sxu@aq4uhc5i5r!vt4vis!%jrjaisyisa2!#upgo*u6r=l9%f"

DEBUG = False

ALLOWED_HOSTS = ['www.loperuv.com', 'www.loperuv.com']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Error
ADMINS = [
    ('chenesan', 'pipio1994@gmail.com'),
]

MANAGERS = [
    ('chenesan', 'pipio1994@gmail.com'),
]
