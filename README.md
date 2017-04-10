#yishan.toys

## Installation

```bash
mkdir [your root directory]
cd [your root directory]
virtualenv .
git clone https://github.com/chenesan/yishan.toys

# for mac osX the installation of uwsgi may fail
# See issue: https://github.com/unbit/uwsgi/issues/1364
# installing and linking libxml2 can fix this
pip install -r yishan.toys/requirement.txt

# You have to set environment variable before using manage.py in local environment:
# 1. `DJANGO_SECRET_KEY`: It's the `SECRET_KEY` in django for data protection. django-admin will generate one when you `startproject`.
# Here you can get your own secret key through
# http://www.miniwebtool.com/django-secret-key-generator/
# or https://docs.djangoproject.com/en/1.9/topics/signing/
# 2. `GOOGLE_ANALYTICS_PROPERTY_ID`: It's id of google analytics. This can be ignored.
# The `local_env.sh` contains the environemnt variable without value. You have to create your own local_env.sh for the next steps
source <your own local_env.sh>
cd yishan_toys

# for the first time you have to migrate to build blog table
python manage.py makemigrations
python manage.py makemigrations blog
python manage.py migrate
# create superuser
python manage.py createsuperuser
# running on port 8000
python manage.py runserver
```

### Production

#### Dependency

* nginx
* uwsgi
* mysql

uwsgi has been installed in the above steps. You have to install nginx and mysql on your own.

configuration files:

* production.env.sh for production environment
* *.cnf for mysql
* nginx.conf for nginx
* yishan_toys.ini for uwsgi
* settings.production.py for django

You have to fill in the environ variable in the above configuration. After that:

```bash
cd [your root directory]

# You have to set environment variable before using manage.py in production environment:
# 1. `DJANGO_SECRET_KEY`: It's the `SECRET_KEY` in django for data protection. django-admin will generate one when you `startproject`.
# Here you can get your own secret key through
# http://www.miniwebtool.com/django-secret-key-generator/
# or https://docs.djangoproject.com/en/1.9/topics/signing/
# 2. `GOOGLE_ANALYTICS_PROPERTY_ID`: It's id of google analytics. This can be ignored.
# The `production_env.sh` contains the environemnt variable without value. You have to create your own production_env.sh for the next steps
source <your own production_env.sh>

uwsgi --ini yishan_toys.ini
```
