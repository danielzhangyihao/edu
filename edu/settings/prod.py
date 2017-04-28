from myproject.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'edu_db',
        'USER': 'yihaozhang',
        'PASSWORD': '19921009',
        'HOST': '',
        'PORT': '',
    }
}