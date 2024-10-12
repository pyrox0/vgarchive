from django.views.generic.detail import DetailView
from django.utils.html import format_html

import django_tables2 as tables
import django_filters as filters
import django_filters.views as filter_views

from vgarchive.models.run import Run
from vgarchive.views import VGArchiveMetaTable, VGArchiveForm


class RunDetailView(DetailView):
    model = Run
    template_name = "vgarchive/detail/run.html"


class RunTable(tables.Table):
    class Meta(VGArchiveMetaTable):
        model = Run
        order_by = "-event"
        exclude = (
            "id",
            "runners",
            "twitch",
        )
        sequence = (
            "game",
            "category",
            "event",
            "length",
            "platform",
            "youtube",
        )

    event = tables.Column(
        linkify=True,
        attrs={"a": {"class": "link link-primary"}},
    )
    youtube = tables.Column(verbose_name="Youtube", orderable=False)
    twitch = tables.Column(verbose_name="Twitch", orderable=False)

    def render_youtube(self, value):  # noqa
        return format_html(
            f'<a class="link text-error" aria-label="Youtube Link" href="{value}"><i class="bi-youtube text-3xl"></i></a>'
        )

    def render_twitch(self, value):  # noqa
        return format_html(
            f'<a class="link text-primary" aria-label="Twitch Link" href="{value}"><i class="bi-twitch text-3xl"></i></a>'
        )


class RunFilter(filters.FilterSet):
    class Meta:
        model = Run
        form = VGArchiveForm
        fields = (
            "game",
            "category",
            "event",
            "platform",
            "runners",
        )


class RunListView(tables.SingleTableMixin, filter_views.FilterView):  # type:ignore
    model = Run
    table_class = RunTable
    template_name = "vgarchive/list/run.html"

    filterset_class = RunFilter
