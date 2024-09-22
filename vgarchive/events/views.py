import locale

from django.db.models import Q
from django.views.generic import DetailView
from django.utils.html import format_html
from django.urls import reverse

import django_tables2 as tables
import django_filters as filters
import django_filters.views as filter_views

from .models import Event

from vgarchive.views import VGArchiveMetaTable, VGArchiveForm
from vgarchive import utils


class EventDetailView(DetailView):
    model = Event
    template_name = "event-detail.html"

    def get_context_data(self, **kwargs) -> dict:  # noqa
        context = super().get_context_data(**kwargs)
        context["runs"] = self.object.run_set.all()
        context["title"] = self.object.name + " | VGArchive"
        return context


class EventTable(tables.Table):
    class Meta(VGArchiveMetaTable):
        model = Event
        order_by = "-name"
        sequence = (
            "name",
            "duration",
            "donation_total",
            "donations",
            "charity",
            "organization",
            "homepage",
            "youtube_playlist",
        )
        exclude = (
            "banner",
            "end_date",
            "id",
            "num_donations",
            "schedule",
            "short_name",
            "source",
            "start_date",
        )

    name = tables.Column(verbose_name="Event Name")
    donation_total = tables.Column(localize=True)
    donations = tables.Column(verbose_name="Donations")
    youtube_playlist = tables.Column(verbose_name="VOD Playlist", orderable=False)
    schedule = tables.Column(
        linkify=True,
        orderable=False,
        attrs={"a": {"class": "link-info external-link"}},
    )
    homepage = utils.views.HomepageColumn(verbose_name="Homepage", orderable=False)
    duration = tables.Column(verbose_name="Time")
    organization = tables.Column(
        linkify=True,
        verbose_name="Organization",
        attrs={"a": {"class": "link link-info"}},
    )
    charity = tables.Column(
        linkify=True,
        verbose_name="Supported Charity",
        attrs={"a": {"class": "link link-info"}},
    )

    def render_donation_total(self, value):  # noqa
        return format_html(
            f'<p class="text-success font-bold">{locale.currency(value, True, True, False)}</p>'
        )

    def order_duration(self, queryset, is_descending):  # noqa
        queryset = queryset.order_by(("-" if is_descending else "") + "start_date")
        return (queryset, True)

    def render_duration(self, record):  # noqa
        return format_html(
            f'<p class="text-info">{record.start_date} to {record.end_date}</p>'
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

    def render_youtube_playlist(self, value):  # noqa
        return format_html(
            f'<a class="link text-error" aria-label="VOD Playlist Link" href="{value}"><i class="bi-youtube text-3xl"></i></a>'
        )


class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        form = VGArchiveForm
        fields = ("name", "charity", "organization")
        exclude = ("homepage", "schedule", "youtube_playlist")

    name = filters.CharFilter(
        label="Name:", lookup_expr="icontains", method="filter_name"
    )

    def filter_name(self, queryset, name, value):  # noqa
        return queryset.filter(
            Q(name__icontains=value) | Q(short_name__icontains=value)
        )


class EventListView(tables.SingleTableMixin, filter_views.FilterView):  # type:ignore
    model = Event
    table_class = EventTable
    template_name = "event-list.html"

    filterset_class = EventFilter
