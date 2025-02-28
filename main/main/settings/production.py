from .base import *
from dotenv import load_dotenv
load_dotenv()

ALLOWED_HOSTS = ['wellforest.ru','www.wellforest.ru','*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
