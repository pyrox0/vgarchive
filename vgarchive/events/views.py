import locale

from django.views.generic.detail import DetailView
from django.utils.html import format_html
from django.urls import reverse

import django_tables2 as tables

from .models import Event


class EventDetailView(DetailView):
    model = Event
    template_name = "event-detail.html"

    def get_context_data(self, **kwargs) -> dict:  # noqa
        context = super().get_context_data(**kwargs)
        context["runs"] = self.object.run_set.all()
        return context


class EventTable(tables.Table):
    class Meta:
        model = Event
        template_name = "vgarchive/table-template.html"
        exclude = ("id", "source", "banner", "organization", "short_name")
        attrs = {  # noqa
            "class": "table text-lg lg:ml-5 lg:max-w-xl",
            "thead": {"class": "text-lg"},
        }

    name = tables.Column(verbose_name="Event Name")
    donation_total = tables.Column(localize=True)

    def render_homepage(self, value):  # noqa
        return format_html(f'<a class="link link-info" href="{value}">Homepage</a>')

    def render_schedule(self, value):  # noqa
        return format_html(f'<a class="link link-info" href="{value}">Schedule</a>')

    def render_donations(self, value):  # noqa
        return format_html(
            f'<a class="link text-success" href="{value}">Donations List</a>'
        )

    def render_youtube_playlist(self, value):  # noqa
        return format_html(
            f'<a class="link text-error" href="{value}">VODs Playlist</a>'
        )

    def render_charity(self, value):  # noqa
        return format_html(
            f'<a class="link link-info" href="{reverse("charity-detail", args=[value.id])}">{value}</a>'
        )

    def render_num_donations(self, value):  # noqa
        return format_html(f'<p class="text-info">{value:n}</p>')

    def value_charity(self, value, record):  # noqa
        return record.charity

    def render_donation_total(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def render_name(self, value, record):  # noqa
        if record.short_name:
            return format_html(
                f'<a class="text-xl font-bold link link-primary" href="{reverse("event-detail", args=[record.id])}">{record.short_name}</a>'
            )

        return format_html(
            f'<a class="text-xl font-bold link link-primary" href="{reverse("event-detail", args=[record.id])}">{value}</a>'
        )


class EventListView(tables.SingleTableView):
    model = Event
    table_class = EventTable
    template_name = "event-list.html"
