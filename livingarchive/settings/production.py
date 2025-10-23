from .base import *
import os

DEBUG = True  # set False in real production

SECRET_KEY = 'django-insecure-bmxu&vi39=^=a^1zto6u5t(1dr1f5a^47_of!+m%p6ar*w5a^v'
MIRAGE_SECRET_KEY = 'gdhhgi%&HGKJ*F___fdffhdjfhsh===%@ghg'

ALLOWED_HOSTS = [
    'indigenousengineering.org.au',
    'livingarchive.teachingforchange.edu.au',
    '127.0.0.1',
    '138.80.128.154',
    'localhost',
]

EMAIL_BACKEND = 'nullmailer.backend.EmailBackend'
WAGTAILADMIN_BASE_URL = "http://localhost:8005"

# Static files
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "home", "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

try:
    from .local import *
except ImportError:
    pass
