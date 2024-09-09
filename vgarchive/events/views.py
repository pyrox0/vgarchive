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
        order_by = "-name"
        sequence = (
            "name",
            "donation_total",
            "donations",
            "charity",
            "organization",
            "homepage",
            "schedule",
            "youtube_playlist",
        )
        exclude = (
            "banner",
            "duration",
            "end_datetime",
            "id",
            "num_donations",
            "short_name",
            "source",
            "start_datetime",
        )
        attrs = {  # noqa
            "class": "table table-lg border-collapse mx-5 border-2 border-base-200 lg:[max-width:calc(100vw-2.5rem)] overflow-x-auto",
            "thead": {"class": "py-4 text-xl border-b-2"},
            "td": {"class": "text-xl"},
            "th": {"class": "border-x-2 border-x-base-200"},
        }

    name = tables.Column(verbose_name="Event Name")
    donation_total = tables.Column(localize=True)
    donations = tables.Column(verbose_name="Donations")
    youtube_playlist = tables.Column(verbose_name="VOD Playlist", orderable=False)
    schedule = tables.Column(orderable=False)
    homepage = tables.Column(orderable=False)
    duration = tables.Column(verbose_name="Time")

    def render_charity(self, value):  # noqa
        return format_html(
            f'<a class="link link-info" href="{reverse("charity-detail", args=[value.id])}">{value}</a>'
        )

    def render_donation_total(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def render_duration(self, value, record):  # noqa
        return format_html(
            f'<p class="text-info">{record.start_datetime} to {record.end_datetime}</p>'
        )

    def render_homepage(self, value):  # noqa
        return format_html(
            f'<a class="external-link link-info" href="{value}">Homepage</a>'
        )

    def render_name(self, value, record):  # noqa
        if record.short_name:
            return format_html(
                f'<a class="text-2xl font-bold link link-primary" href="{reverse("event-detail", args=[record.id])}">{record.short_name}</a>'
            )

        return format_html(
            f'<a class="text-2xl font-bold link link-primary" href="{reverse("event-detail", args=[record.id])}">{value}</a>'
        )

    def render_donations(self, value, record):  # noqa
        return format_html(
            f'<a href="{value}" class="external-link link-info">{record.num_donations:n}</a>'
        )

    def render_organization(self, value):  # noqa
        return format_html(
            f'<a class="link link-info" href="{reverse("organization-detail", args=[value.id])}">{value}</a>'
        )

    def render_schedule(self, value):  # noqa
        return format_html(
            f'<a class="link-info external-link" href="{value}">Schedule</a>'
        )

    def render_youtube_playlist(self, value):  # noqa
        return format_html(
            f'<a class="link text-error" aria-label="VOD Playlist Link" href="{value}"><i class="bi-youtube text-3xl"></i></a>'
        )

    def value_charity(self, value, record):  # noqa
        return record.charity


class EventListView(tables.SingleTableView):
    model = Event
    table_class = EventTable
    template_name = "event-list.html"
