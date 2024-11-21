from .base import *

import google.cloud.logging
from google.cloud.logging import DESCENDING

client = google.cloud.logging.Client()
client.setup_logging()

DEBUG = False
ALLOWED_HOSTS = ['blood-bank-442312.uc.r.appspot.com', 'blood-bank-442312@appspot.gserviceaccount.com','blood-bank-121963256536.us-central1.run.app']


ROOT_URLCONF = 'bloodbankmanagement.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'your_db_name'),
        'USER': os.getenv('DB_USER', 'your_db_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_db_password'),
        'HOST': os.getenv('DB_HOST', 'your_db_host'),
        'PORT': os.getenv('DB_PORT', 'your_db_port'),
    }
}

# Static files (e.g. for serving via a CDN or on the server)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'blood-bank-442312.appspot.com'
# Logging settings for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'google_cloud': {
            'level': 'INFO',
            'class': 'google.cloud.logging.handlers.CloudLoggingHandler',
            'client': client,  # Ensure the client is passed correctly
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['google_cloud', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}



# Security settings for production
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
