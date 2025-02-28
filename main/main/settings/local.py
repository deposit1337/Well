from .base import *
from django.core.cache import cache
ALLOWED_HOSTS = ['wellforest.ru','www.wellforest.ru','*']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# cache.clear()