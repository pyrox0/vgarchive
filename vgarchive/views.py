from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


class Home(TemplateView):
    template_name = "vgarchive/index.html"


class Search(FormView):
    template_name = "vgarchive/search.html"
