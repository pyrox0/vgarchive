from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Run


class RunDetailView(DetailView):
    model = Run
    template_name = "runs/detail.html"


class RunListView(ListView):
    model = Run
    paginate_by = 20
    template_name = "runs/list.html"
