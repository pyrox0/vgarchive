import os

from vgarchive.settings.common import *

from vgarchive.settings import common

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5pvrv(*#6@e=sk3&=zt6znv^0#9(b+5weaws_6et&fuph3*n#6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ["*"]

INSTALLED_APPS = common.INSTALLED_APPS + [
    "django.contrib.staticfiles",
    # Admin shell
    "django_admin_shell",
    # Hot reload
    "django_browser_reload",
    # Debug toolbar
    "debug_toolbar",
    "template_profiler_panel",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Minify HTML
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    # Compression
    "compression_middleware.middleware.CompressionMiddleware",
    # Hot reload
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    # Debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # Minify HTML
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # admindocs
    "django.contrib.admindocs.middleware.XViewMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db/vgarchive.db",
    }
}

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded")

# django.contrib.staticfiles
STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]


# Force toolbar to show in dev
def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.alerts.AlertsPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "template_profiler_panel.panels.template.TemplateProfilerPanel",
]
