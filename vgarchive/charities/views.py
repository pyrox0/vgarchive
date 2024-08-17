from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Charity


class CharityDetailView(DetailView):
    model = Charity
    template_name = "charities/detail.html"


class CharityListView(ListView):
    model = Charity
    paginate_by = 20
    template_name = "charities/list.html"
