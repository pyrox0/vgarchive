from django.urls import path

from .views import MarathonDetailView, MarathonListView

urlpatterns = [
    path("<slug:pk>/", MarathonDetailView.as_view(), name="marathon-details"),
    path("", MarathonListView.as_view(), name="marathon-list"),
]
