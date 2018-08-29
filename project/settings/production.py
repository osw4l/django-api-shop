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
        'NAME': 'd866nejv34qi4m',
        'USER': 'pauttcyslclvsf',
        'PASSWORD': 'a395c2f6e8adb53f6efdbf078bfba7b3cee82614e053fafef974dcf7a6a16911clear',
        'HOST': 'ec2-50-17-194-129.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
