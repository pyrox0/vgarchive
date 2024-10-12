from django.urls import path, re_path, include
from django.contrib.admin import site as admin_site
from django.conf import settings

from debug_toolbar.toolbar import debug_toolbar_urls

from .views import Home, RunnerIngest, RunIngest
from .views.charity import CharityDetailView, CharityListView

urlpatterns = [
    # Admindoc
    path("admin/doc/", include("django.contrib.admindocs.urls"), name="admindoc"),
    # Admin
    path("admin/", admin_site.urls),
    # VGArchive
    re_path(r"^organizations/", include("vgarchive.organizations.urls")),
    re_path(r"^events/", include("vgarchive.events.urls")),
    # Charities
    path("charities/<slug:pk>/", CharityDetailView.as_view(), name="charity-detail"),
    path("charities/", CharityListView.as_view(), name="charity-list"),
    re_path(r"^runs/", include("vgarchive.runs.urls")),
    # Ingest Views
    path("ingest/runners", RunnerIngest.as_view(), name="ingest-runner"),
    path("ingest/runs", RunIngest.as_view(), name="ingest-run"),
    # Hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Index
    path("", Home.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns.insert(0, re_path(r"^admin/shell/", include("django_admin_shell.urls")))
    urlpatterns += debug_toolbar_urls()
