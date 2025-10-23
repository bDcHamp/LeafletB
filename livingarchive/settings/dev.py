from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bmxu&vi39=^=a^1zto6u5t(1dr1f5a^47_of!+m%p6ar*w5a^v'
MIRAGE_SECRET_KEY = 'gdhhgi%&HGKJ*F___fdffhdjfhsh===%@ghg'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*','localhost'] 

WAGTAILADMIN_BASE_URL="http://localhost:8002"

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'Stories of Country <{}>'.format(os.getenv('EMAIL_HOST_USER'))
SERVER_EMAIL = os.getenv('EMAIL_HOST_USER')

# Allauth email settings
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Stories of Country] '
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

# Enable email logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.core.mail': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Django-allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Site settings
SITE_ID = 1
from django.contrib.sites.models import Site
Site.objects.update_or_create(
    id=1,
    defaults={
        'domain': '127.0.0.1:8005',
        'name': 'Stories of Country'
    }
)

try:
    from .local import *
except ImportError:
    pass
