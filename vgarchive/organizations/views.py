from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Organization


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organizations/detail.html"


class OrganizationListView(ListView):
    model = Organization
    paginate_by = 20
    template_name = "organizations/list.html"
