from django.urls import path, re_path, include
from django.contrib.admin import site as admin_site
from django.conf import settings

from debug_toolbar.toolbar import debug_toolbar_urls

from .views import Home
from .views.create import (
    CharityCreate,
    EventCreate,
    GameCreate,
    OrganizationCreate,
    RunnerCreate,
    RunCreate,
)
from .views.charity import CharityDetailView, CharityListView
from .views.event import EventDetailView, EventListView
from .views.organization import OrganizationDetailView, OrganizationListView
from .views.run import RunDetailView, RunListView

__all__ = ["urlpatterns"]

urlpatterns = [
    # Admindoc
    path("admin/doc/", include("django.contrib.admindocs.urls"), name="admindoc"),
    # Admin
    path("admin/", admin_site.urls),
    # Organizations
    path(
        "organizations/<slug:pk>/",
        OrganizationDetailView.as_view(),
        name="organization-detail",
    ),
    path("organizations/", OrganizationListView.as_view(), name="organization-list"),
    # Events
    path("events/<slug:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("events/", EventListView.as_view(), name="event-list"),
    # Charities
    path("charities/<slug:pk>/", CharityDetailView.as_view(), name="charity-detail"),
    path("charities/", CharityListView.as_view(), name="charity-list"),
    # Runs
    path("runs/<slug:pk>/", RunDetailView.as_view(), name="run-detail"),
    path("runs/", RunListView.as_view(), name="run-list"),
    # Manual Creation Views
    path("create/charity", CharityCreate.as_view(), name="create-charity"),
    path("create/event", EventCreate.as_view(), name="create-event"),
    path("create/game", GameCreate.as_view(), name="create-game"),
    path(
        "create/organization", OrganizationCreate.as_view(), name="create-organization"
    ),
    path("create/runner", RunnerCreate.as_view(), name="create-runner"),
    path("create/run", RunCreate.as_view(), name="create-run"),
    # Hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Index
    path("", Home.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns.insert(0, re_path(r"^admin/shell/", include("django_admin_shell.urls")))
    urlpatterns += debug_toolbar_urls()
