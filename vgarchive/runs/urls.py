from django.urls import path

from .views import RunDetailView, RunListView

urlpatterns = [
    path("<slug:pk>/", RunDetailView.as_view(), name="run-details"),
    path("", RunListView.as_view(), name="run-list"),
]
