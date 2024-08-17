from django.urls import path

from .views import CharityDetailView, CharityListView

urlpatterns = [
    path("<slug:pk>/", CharityDetailView.as_view(), name="charity-details"),
    path("", CharityListView.as_view(), name="charity-list"),
]
