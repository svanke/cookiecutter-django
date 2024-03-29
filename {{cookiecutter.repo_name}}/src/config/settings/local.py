import os

from .base import *
from .base import env

# Secret key doesn't matter in local development
# SECRET_KEY = 'some-keys'
SECRET_KEY = env('SECRET_KEY', default="!!!SET DJANGO SECRET KEY",)

# Debug mode
DEBUG = env.bool('DEBUG', False)

# Allowed from all host
ALLOWED_HOSTS = ['*']

# App specifically for development
INSTALLED_APPS += [
    # 'debug_toolbar',
    'django_extensions',
]

# Middleware for development
MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware'
]

# Database configuration
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "django.db.backends.sqlite3"),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("DJANGO_DATABASE_HOST", "localhost"),
        "PORT": os.environ.get("DJANGO_DATABASE_PORT", "5432"),
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Django REST Framework Cors Header Origin
CORS_ORIGIN_ALLOW_ALL = True

# Static files
STATIC_ROOT = str(ROOT_DIR / 'static_files')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(ROOT_DIR / 'static'),
)
# COMPRESS_ROOT = ROOT_DIR / 'static'
# COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
)

# Media files
MEDIA_ROOT = str(ROOT_DIR / 'media')
MEDIA_URL = '/media/'

# Login URL
LOGIN_URL = '/login'
