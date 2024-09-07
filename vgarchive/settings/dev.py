from vgarchive.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5pvrv(*#6@e=sk3&=zt6znv^0#9(b+5weaws_6et&fuph3*n#6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    # Hot reload
    "django_browser_reload",
]

MIDDLEWARE += [
    # Hot reload
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/vgarchive.db",
    }
}
