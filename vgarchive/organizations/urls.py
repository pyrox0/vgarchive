from django.urls import path

from .views import OrganizationDetailView, OrganizationListView

urlpatterns = [
    path("<slug:pk>/", OrganizationDetailView.as_view(), name="organization-details"),
    path("", OrganizationListView.as_view(), name="organization-list"),
]
