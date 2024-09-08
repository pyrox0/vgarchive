from django.urls import path

from .views import EventDetailView, EventListView

urlpatterns = [
    path("<slug:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("", EventListView.as_view(), name="event-list"),
]
