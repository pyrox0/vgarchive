"""
URL configuration for vgarchive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from django.contrib.admin import site as admin_site
from django.conf import settings

from debug_toolbar.toolbar import debug_toolbar_urls

from .views import Home, Search

urlpatterns = [
    # Admindoc
    path("admin/doc/", include("django.contrib.admindocs.urls"), name="admindoc"),
    # Admin
    path("admin/", admin_site.urls),
    # Marathons
    re_path(r"^organization/", include("vgarchive.organizations.urls")),
    re_path(r"^event/", include("vgarchive.events.urls")),
    re_path(r"^charity/", include("vgarchive.charities.urls")),
    re_path(r"^run/", include("vgarchive.runs.urls")),
    path("search/", Search.as_view(), name="search"),
    # Hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Index
    path("", Home.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns.insert(0, re_path(r"^admin/shell/", include("django_admin_shell.urls")))
    urlpatterns += debug_toolbar_urls()
