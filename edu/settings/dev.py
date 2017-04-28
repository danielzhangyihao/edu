from edu.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'edu_db',
        'USER': 'jeffdh5',
        'HOST': '',
        'PORT': '',
    }
}
