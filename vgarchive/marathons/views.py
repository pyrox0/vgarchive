from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Marathon


class MarathonDetailView(DetailView):
    model = Marathon
    template_name = "marathons/detail.html"


class MarathonListView(ListView):
    model = Marathon
    paginate_by = 20
    template_name = "marathons/list.html"
