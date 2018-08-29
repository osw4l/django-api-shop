from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [

]

WSGI_APPLICATION = 'project.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

CORS_ORIGIN_ALLOW_ALL = True
