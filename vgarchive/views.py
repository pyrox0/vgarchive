from django import forms
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView

from vgarchive.runs.models import Runner


class VGArchiveMetaTable:
    template_name = "vgarchive/table-template.html"
    attrs = {  # noqa
        "class": "table table-zebra table-lg border-collapse lg:mx-5 border-2 border-base-200 lg:[max-width:calc(100vw-2.5rem)] overflow-x-auto",
        "thead": {"class": "py-4 text-xl border-b-2"},
        "td": {"class": "text-xl"},
        "th": {"class": "border-x-2 border-x-base-200"},
    }


class VGArchiveForm(forms.Form):
    template_name = "django/forms/div.html"  # type:ignore


class Home(TemplateView):
    template_name = "vgarchive/index.html"


class Search(FormView):
    template_name = "vgarchive/search.html"


class RunnerIngest(CreateView):
    model = Runner
    fields = (
        "name",
        "pronouns",
        "twitch",
        "youtube",
        "twitter",
        "bluesky",
    )

    template_name = "vgarchive/forms/runner-ingest.html"
