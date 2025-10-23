from .production import *

# Development settings override

# Always keep debug on locally
DEBUG = True

# Only allow local access
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Use console backend so emails print to terminal instead of sending
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Optional: use SQLite for local dev (if you don’t want to touch prod DB)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }

# Static files (for development, Django serves them automatically)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
