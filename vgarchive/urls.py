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

from .views import Home, Search

urlpatterns = [
    # Admindoc
    path("admin/doc/", include("django.contrib.admindocs.urls"), name="admindoc"),
    # Admin
    path("admin/", admin_site.urls),
    # Marathons
    re_path(r"^marathons?/", include("vgarchive.marathons.urls")),
    re_path(r"^events?/", include("vgarchive.events.urls")),
    re_path(r"^(charity|charities)/", include("vgarchive.charities.urls")),
    re_path(r"^runs?/", include("vgarchive.runs.urls")),
    path("search/", Search.as_view(), name="search"),
    # Hot reload
    path("__reload__/", include("django_browser_reload.urls")),
    # Index
    path("", Home.as_view(), name="home"),
]
