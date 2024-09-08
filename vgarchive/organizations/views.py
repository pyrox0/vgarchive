from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Organization
from vgarchive.charities.models import Charity


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "organization-detail.html"

    def get_context_data(self, **kwargs) -> dict:  # noqa
        # Get context
        context = super().get_context_data(**kwargs)
        context["events"] = self.object.event_set.all()
        context["charities"] = Charity.objects.filter(  # type:ignore
            id__in=context["events"].values_list("charity", flat=True)
        )
        return context


class OrganizationListView(ListView):
    model = Organization
    paginate_by = 20
    template_name = "organization-list.html"
