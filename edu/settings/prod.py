from edu.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'edu_prod_db',
        'USER': 'edu',
        'PASSWORD': '19921009',
        'HOST': 'localhost',
        'PORT': '',
    }
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/prod/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','47.94.232.35']