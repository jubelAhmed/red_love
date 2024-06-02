from donation.settings.base import *

import os
from dotenv import load_dotenv

# Load environment variables from .os.getenv file
load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME","d"),
        'USER': os.getenv("DB_USER","d"),
        'PASSWORD': os.getenv("DB_PASSWORD","d"),
        'HOST': os.getenv("DB_HOST","d"),
        'PORT': os.getenv("DB_PORT","d"),
    }
}
# Security settings
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# Static and media settings
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
