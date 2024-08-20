from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Organization
from vgarchive.events.models import Event


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organizations/detail.html"

    def get_context_data(self, **kwargs):
        # Get context
        context = super().get_context_data(**kwargs)
        context["events"] = Event.objects.filter(organization=self.kwargs.get("pk"))
        return context


class OrganizationListView(ListView):
    model = Organization
    paginate_by = 20
    template_name = "organizations/list.html"
