from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Event


class EventDetailView(DetailView):
    model = Event
    template_name = "event-detail.html"


class EventListView(ListView):
    model = Event
    paginate_by = 20
    template_name = "event-list.html"
