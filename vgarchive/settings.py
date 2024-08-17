"""
Django settings for vgarchive project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5pvrv(*#6@e=sk3&=zt6znv^0#9(b+5weaws_6et&fuph3*n#6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]
INTERNAL_IPS = ["127.0.0.1", "[::1]"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Allauth, for discord accounts
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.discord",
    # Django-ninja for API stuff
    "ninja",
    # All our custom apps
    "vgarchive",
    "vgarchive.charities",
    "vgarchive.events",
    "vgarchive.marathons",
    "vgarchive.runs",
    # Tailwind CSS
    "tailwind",
    "vgarchive.theme",
    # Bootstrap Icons
    "django_bootstrap_icons",
    # Reusable components support
    "slippers",
    # Hot reload
    "django_browser_reload",
]

TAILWIND_APP_NAME = "vgarchive.theme"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # allauth
    "allauth.account.middleware.AccountMiddleware",
    # admindocs
    "django.contrib.admindocs.middleware.XViewMiddleware",
    # Hot reload
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "vgarchive.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "vgarchive/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # Autoload slippers every time
            "builtins": ["slippers.templatetags.slippers"],
        },
    },
]

ASGI_APPLICATION = "vgarchive.asgi.application"

# Allow allauth to handle authentication

AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/vgarchive.db",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# User-uploaded files

MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")


# Bootstrap Icons Configuration

# BS_ICONS_CACHE = os.path.join(STATIC_ROOT, "icon_cache")

BS_ICONS_BASE_PATH = "vgarchive/static/bs_icons/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
