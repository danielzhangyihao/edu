from edu.settings.base import *

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

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/prod/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json'),
    }
}

ALLOWED_HOSTS = ['www.51yaoguo.com', '51yaoguo.com']