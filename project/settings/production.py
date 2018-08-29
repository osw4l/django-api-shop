from .base import *

DEBUG = True

INSTALLED_APPS += ('gunicorn',)

ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

WSGI_APPLICATION = 'project.wsgi.production.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddmr1v46q1m5k0',
        'USER': 'hjzjicushthugd',
        'PASSWORD': '6976a3090a9e532d0643d9e388c3a125157b85f3c32908088766a3f45da12ca4',
        'HOST': 'ec2-54-83-13-119.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
