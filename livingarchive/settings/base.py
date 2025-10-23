"""
Django base settings for livingarchive project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Load environment variables
load_dotenv(os.path.join(PROJECT_DIR, "settings", ".env"))
api_key = str(os.getenv("API_KEY"))

PASSWORD_REQUIRED_TEMPLATE = "password_required.html"

# -------------------------------------------------------------------
# Wagtail Google Maps
# -------------------------------------------------------------------
WAGTAIL_ADDRESS_MAP_CENTER = "Australia"
WAGTAIL_ADDRESS_MAP_KEY = api_key

# -------------------------------------------------------------------
# Application definition
# -------------------------------------------------------------------
INSTALLED_APPS = [
    "home",
    "search",
    "wagtailgmaps",
    "blog",
    "wagtailmedia",
    "wagtailvideos",
    #"wagtail.contrib.modeladmin",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.search_promotions",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "captcha",
    "wagtailcaptcha",
    "wagtailmenus",
    "user_group_management",
    "modelcluster",
    "taggit",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "livingarchive",
]


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",      # keep Django admin login
    "allauth.account.auth_backends.AuthenticationBackend",  # allauth
]

SITE_ID = 1

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "blog.middleware.PagePasswordUpdateMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "livingarchive.urls"

# -------------------------------------------------------------------
# Templates
# -------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),  # global templates folder
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "templatetag": "blog.templatetags.to_at",
            },
        },
    },
]

# -------------------------------------------------------------------
# Authentication
# -------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Default
    "allauth.account.auth_backends.AuthenticationBackend",  # Allauth
]

WSGI_APPLICATION = "livingarchive.wsgi.application"

# -------------------------------------------------------------------
# Database
# -------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# -------------------------------------------------------------------
# Password validation
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------------------------------------------
# Internationalization
# -------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# -------------------------------------------------------------------
STATIC_URL = "/static/"

# Your own project-wide static folder (where CSS/JS/images live)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Where collectstatic will put all static files (for production)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Storage backend (fine for dev, you may change in production)
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# -------------------------------------------------------------------
# Media files (user uploads)
# -------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Temp upload directory
FILE_UPLOAD_TEMP_DIR = os.path.join(PROJECT_DIR, "tmp")

# -------------------------------------------------------------------
# Wagtail settings
# -------------------------------------------------------------------
WAGTAIL_SITE_NAME = "livingarchive"
WAGTAIL_CACHE = False

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# -------------------------------------------------------------------
# Auth settings (Allauth)
# -------------------------------------------------------------------
# URLs
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'

# Authentication
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True

# Security
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # 5 minutes
ACCOUNT_USERNAME_BLACKLIST = ["admin", "moderator", "editor"]

# User Experience
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True

# Forms
WAGTAIL_FRONTEND_LOGIN_TEMPLATE = "account/login.html"

# -------------------------------------------------------------------
# Recaptcha
# -------------------------------------------------------------------
RECAPTCHA_PUBLIC_KEY = "6LfsIJYjAAAAAMOjW3Ysb4IdNQyxRatxcu1PmavL"
RECAPTCHA_PRIVATE_KEY = "6LfsIJYjAAAAAJMlLIzgjkOXPAdnqffi1syvL3o2"
NOCAPTCHA = True

# -------------------------------------------------------------------
# Email settings
# -------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
SERVER_EMAIL = os.getenv('EMAIL_HOST_USER')

# -------------------------------------------------------------------
# Default primary key
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
